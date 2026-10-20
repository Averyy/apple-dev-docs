# NSFontCollection

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A font collection, which is a group of font descriptors taken together as a single object.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class NSFontCollection
```

```objc
@interface NSFontCollection : NSObject
```

#### Overview

You can publicize the font collection as a named collection and it is presented through the System user interface such as the font panel and Font Book. The queries can be modified using the [`NSMutableFontCollection`](./nsmutablefontcollection.md) subclass.

## Topics

### Creating Font Collections
- [init(descriptors: [NSFontDescriptor])](./nsfontcollection/init%28descriptors%29.md)
  Returns a font collection matching the given descriptors.
- [init?(locale: Locale)](./nsfontcollection/init%28locale%29.md)
  Returns a collection of fonts matching the given locale.
- [init?(name: NSFontCollection.Name)](./nsfontcollection/init%28name%29.md)
  Creates a named font collection object.
- [init?(name: NSFontCollection.Name, visibility: NSFontCollection.Visibility)](./nsfontcollection/init%28name,visibility%29.md)
  Creates a font collection with the specified name and font visibility.
- [class var withAllAvailableDescriptors: NSFontCollection](./nsfontcollection/withallavailabledescriptors.md)
  The font collection that matches all registered fonts.
### Naming the Font Collection
- [class func rename(fromName: NSFontCollection.Name, visibility: NSFontCollection.Visibility, toName: NSFontCollection.Name) throws](./nsfontcollection/rename%28fromname,visibility,toname%29.md)
  Renames the font collection with the specified name and visibility to the second name specified.
- [class func show(NSFontCollection, withName: NSFontCollection.Name, visibility: NSFontCollection.Visibility) throws](./nsfontcollection/show%28_,withname,visibility%29.md)
  Make the given font collection visible by giving it a name.
- [class func hide(withName: NSFontCollection.Name, visibility: NSFontCollection.Visibility) throws](./nsfontcollection/hide%28withname,visibility%29.md)
  Remove from view the named font collection with the specified visibility.
- [class var allFontCollectionNames: [NSFontCollection.Name]](./nsfontcollection/allfontcollectionnames.md)
  Returns all named collections visible to this process.
- [NSFontCollection.Name](./nsfontcollection/name.md)
  The constants represent the standard mutable collection names—these names are included in the list of [`allFontCollectionNames`](./nsfontcollection/allfontcollectionnames.md)–they have special meaning to the Cocoa font system and should not be hidden or renamed.
- [NSFontCollection.Visibility](./nsfontcollection/visibility.md)
  Constants that specify the visibility of font collections.
### Getting the Font Descriptors
- [var matchingDescriptors: [NSFontDescriptor]?](./nsfontcollection/matchingdescriptors.md)
  An array of font descriptors matching the logical descriptors.
- [func matchingDescriptors(forFamily: String) -> [NSFontDescriptor]?](./nsfontcollection/matchingdescriptors%28forfamily%29.md)
  Returns an array of font descriptors matching the logical descriptors for the given font family.
- [func matchingDescriptors(forFamily: String, options: [NSFontCollectionMatchingOptionKey : NSNumber]?) -> [NSFontDescriptor]?](./nsfontcollection/matchingdescriptors%28forfamily,options%29.md)
  Returns an array of font descriptors matching the logical descriptors for the given font family and options.
- [func matchingDescriptors(options: [NSFontCollectionMatchingOptionKey : NSNumber]?) -> [NSFontDescriptor]?](./nsfontcollection/matchingdescriptors%28options%29.md)
  Returns an array of font descriptors matching the logical descriptors with the given options.
- [struct NSFontCollectionMatchingOptionKey](./nsfontcollectionmatchingoptionkey.md)
  These constants are used by the [`matchingDescriptors(options:)`](./nsfontcollection/matchingdescriptors%28options%29.md) and [`matchingDescriptors(forFamily:options:)`](./nsfontcollection/matchingdescriptors%28forfamily,options%29.md) options dictionary parameters.
- [var queryDescriptors: [NSFontDescriptor]?](./nsfontcollection/querydescriptors.md)
  An array of font descriptors whose matching results produce the collection’s matching descriptors.
- [var exclusionDescriptors: [NSFontDescriptor]?](./nsfontcollection/exclusiondescriptors.md)
  A list of query font descriptors whose matching results are excluded from the list of matching descriptors.
### Responding to Changes
- [class let didChangeNotification: NSNotification.Name](./nsfontcollection/didchangenotification.md)
  Posted whenever a font collection is changed.
- [NSFontCollection.UserInfoKey](./nsfontcollection/userinfokey.md)
  These constants are used as keys in the [`didChangeNotification`](./nsfontcollection/didchangenotification.md) `userInfo` dictionary to indicate the changes that have taken place.
- [NSFontCollection.ActionTypeKey](./nsfontcollection/actiontypekey.md)
  The following actions are possible values of the [`actionUserInfoKey`](./nsfontcollection/actionuserinfokey.md) in the [`didChangeNotification`](./nsfontcollection/didchangenotification.md) `userInfo` method.
### Structures
- [NSFontCollection.DidChangeMessage](./nsfontcollection/didchangemessage.md)
### Initializers
- [init?(coder: NSCoder)](./nsfontcollection/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [NSMutableFontCollection](./nsmutablefontcollection.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSMutableCopying](../Foundation/nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Management
- [class NSFontManager](./nsfontmanager.md)
  The center of activity for the font-conversion system.
- [class NSMutableFontCollection](./nsmutablefontcollection.md)
  A mutable collection of font descriptors taken together as a single object.
- [struct NSFontCollectionOptions](./nsfontcollectionoptions.md)
  Constants that support font collection management.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontcollection)*