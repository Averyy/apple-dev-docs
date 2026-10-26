# Supporting Conversions with Scripting Class Extensions

**Framework**: Professional-Video-Applications  
**Role**: Article

Support conversions between the Apple event descriptor types and Foundation object classes.

#### Overview

If your app uses Cocoa Scripting support to handle Apple events sent by Final Cut Pro, it must support conversions between certain Apple event descriptor types used by Final Cut Pro and the respective Foundation classes. These conversions are not supported by Cocoa Scripting.

The following code snippets provide interfaces for the required conversions.

Apple event record descriptor (`typeAERecord`) and `NSDictionary`:

```swift
@interface NSDictionary (UserDefinedRecord)
  +(NSDictionary*)scriptingUserDefinedRecordWithDescriptor:(NSAppleEventDescriptor*)desc;
  -(NSAppleEventDescriptor*)scriptingUserDefinedRecordDescriptor;
@end
```

Apple event list descriptor (`typeAEList`) and `NSArray`:

```swift
@interface NSArray (UserList)
  +(NSArray*)scriptingUserListWithDescriptor:(NSAppleEventDescriptor*)desc;
  -(NSAppleEventDescriptor*)scriptingUserListDescriptor;
@end
```

Apple event generic descriptor (`list`, `record`, and so on) and `id`:

```swift
@interface NSAppleEventDescriptor (GenericObject)
  +(NSAppleEventDescriptor*)descriptorWithObject:(id)object;
  -(id)objectValue;
@end
```

The following is an example implementation of the above interface. For more information, see the [`NSAppleEventDescriptor`](../Foundation/nsappleeventdescriptor.md) Class Reference.

```swift
#import "ScriptingSupportCategories.h"
 
#import <Carbon/Carbon.h>
 
 
@implementation NSDictionary (UserDefinedRecord)
 
+(NSDictionary*)scriptingUserDefinedRecordWithDescriptor:(NSAppleEventDescriptor*)desc
{
    NSMutableDictionary* dict = [NSMutableDictionary dictionaryWithCapacity:0];
    NSAppleEventDescriptor* userFieldItems = [desc descriptorForKeyword:keyASUserRecordFields];
    NSInteger numItems = [userFieldItems numberOfItems];
 
    for ( NSInteger itemIndex = 1; itemIndex <= numItems - 1; itemIndex += 2 ) {
        NSAppleEventDescriptor* keyDesc = [userFieldItems descriptorAtIndex:itemIndex];
        NSAppleEventDescriptor* valueDesc = [userFieldItems descriptorAtIndex:itemIndex + 1];
        NSString* keyString = [keyDesc stringValue];
        id value = [valueDesc objectValue];
 
        if ( keyString != nil && value != nil )
            [dict setObject:value forKey:keyString];
    }
 
    return [NSDictionary dictionaryWithDictionary:dict];
}
 
-(NSAppleEventDescriptor*)scriptingUserDefinedRecordDescriptor
{
    NSAppleEventDescriptor* recordDesc = [NSAppleEventDescriptor recordDescriptor];
    NSAppleEventDescriptor* userFieldDesc = [NSAppleEventDescriptor listDescriptor];
    NSInteger userFieldIndex = 1;
 
    for ( id key in self ) {
        if ( [key isKindOfClass:[NSString class]] ) {
            NSString* valueString = nil;
            id value = [self objectForKey:key];
 
            if ( ! [value isKindOfClass:[NSString class]] )
                valueString = [NSString stringWithFormat:@"%@", value];
            else
                valueString = value;
 
            NSAppleEventDescriptor* valueDesc = [NSAppleEventDescriptor descriptorWithString:valueString];
            NSAppleEventDescriptor* keyDesc = [NSAppleEventDescriptor descriptorWithString:key];
 
            if ( valueDesc != nil && keyDesc != nil ) {
                [userFieldDesc insertDescriptor:keyDesc atIndex:userFieldIndex++];
                [userFieldDesc insertDescriptor:valueDesc atIndex:userFieldIndex++];
            }
        }
    }
 
    [recordDesc setDescriptor:userFieldDesc forKeyword:keyASUserRecordFields];
 
    return recordDesc;
}
 
 
@end
 
@implementation NSArray (UserList)
 
+(NSArray*)scriptingUserListWithDescriptor:(NSAppleEventDescriptor*)desc
{
    NSMutableArray* array = [NSMutableArray arrayWithCapacity:0];
    NSInteger numItems = [desc numberOfItems];
 
    for ( NSInteger itemIndex = 1; itemIndex <= numItems; itemIndex++ ) {
        NSAppleEventDescriptor* itemDesc = [desc descriptorAtIndex:itemIndex];
 
        [array addObject:[itemDesc objectValue]];
    }
 
    return [NSArray arrayWithArray:array];
}
 
-(NSAppleEventDescriptor*)scriptingUserListDescriptor
{
    NSAppleEventDescriptor* listDesc = [NSAppleEventDescriptor listDescriptor];
    NSInteger itemIndex = 1;
 
    for ( id item in self ) {
        NSAppleEventDescriptor* itemDesc = [NSAppleEventDescriptor descriptorWithObject:item];
 
        [listDesc insertDescriptor:itemDesc atIndex:itemIndex++];
    }
 
    return listDesc;
}
 
@end
 
 
@implementation NSAppleEventDescriptor (GenericObject)
 
+(NSAppleEventDescriptor*)descriptorWithObject:(id)object
{
    NSAppleEventDescriptor* desc = nil;
 
    if ( [object isKindOfClass:[NSArray class]] ) {
        NSArray*    array = (NSArray*)object;
 
        desc = [array scriptingUserListDescriptor];
    }
    else if ( [object isKindOfClass:[NSDictionary class]] ) {
        NSDictionary*   dict = (NSDictionary*)object;
 
        desc = [dict scriptingUserDefinedRecordDescriptor];
    }
    else if ( [object isKindOfClass:[NSString class]] ) {
        desc = [NSAppleEventDescriptor descriptorWithString:(NSString*)object];
    }
    else if ( [object isKindOfClass:[NSURL class]] ) {
        desc = [NSAppleEventDescriptor descriptorWithURL:(NSURL*)object];
    }
    else {
        NSString* valueString = [NSString stringWithFormat:@"%@", object];
 
        desc = [NSAppleEventDescriptor descriptorWithString:valueString];
    }
 
    return desc;
}
 
-(id)objectValue
{
    DescType    descType = [self descriptorType];
    DescType    bigEndianDescType = 0;
    id          object = nil;
 
 
    switch ( descType ) {
        case typeUnicodeText:
        case typeUTF8Text:
            object = [self stringValue];
            break;
        case typeFileURL:
            object = [self fileURLValue];
            break;
        case typeAEList:
            object = [NSArray scriptingUserListWithDescriptor:self];
            break;
        case typeAERecord:
            object = [NSDictionary scriptingUserDefinedRecordWithDescriptor:self];
            break;
        case typeSInt16:
        case typeUInt16:
        case typeSInt32:
        case typeUInt32:
        case typeSInt64:
        case typeUInt64:
            object = [NSNumber numberWithInteger:(NSInteger)[self int32Value]];
            break;
        default:
            bigEndianDescType = EndianU32_NtoB(descType);
            NSLog(@"Creating NSData for AE desc type %.4s.", (char*)&bigEndianDescType);
            object = [self data];
            break;
    }
 
    return object;
}
 
@end
```

## See Also

### Handling Apple Events
- [Responding to Apple Events from Final Cut Pro](./responding-to-apple-events-from-final-cut-pro.md)
  Tell Final Cut Pro about the kind of data your users want to receive in your app through a custom share destination.
- [Creating Scripting Definitions for Custom Share Destinations](./creating-scripting-definitions-for-custom-share-destinations.md)
  Define the record types, object classes, and event types that let your app interact with Final Cut Pro.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/supporting-conversions-with-scripting-class-extensions)*