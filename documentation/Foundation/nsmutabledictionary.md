# NSMutableDictionary

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

A dynamic collection of objects associated with unique keys.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSMutableDictionary
```

```objc
@interface NSMutableDictionary : NSDictionary
```

## Overview

In Swift, you can use this type instead of a [`Dictionary`](../Swift/dictionary.md) variable in cases that require reference semantics.

The `NSMutableDictionary` class declares the programmatic interface to objects that manage mutable associations of keys and values. It adds modification operations to the basic operations it inherits from [`NSDictionary`](./nsdictionary.md).

`NSMutableDictionary` is “toll-free bridged” with its Core Foundation counterpart, [`CFMutableDictionary`](../CoreFoundation/cfmutabledictionary.md). See [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information on toll-free bridging.

### Setting Values Using Subscripting

In addition to the provided instance methods, such as [`setObject(_:forKey:)`](./nsmutabledictionary/setobject%28_,forkey%29.md), you can access `NSDictionary` values by their keys using *subscripting*.

**Swift**:

```swift
let value = "someValue"
mutableDictionary["someKey"] = value
```

**Objective-C**:

```objc
id value = @"someValue";
mutableDictionary[@"someKey"] = value;
```

### Subclassing Notes

There should typically be little need to subclass `NSMutableDictionary`. If you do need to customize behavior, it is often better to consider composition rather than subclassing.

#### Methods to Override

In a subclass, you must override both of its primitive methods:

- [`setObject(_:forKey:)`](./nsmutabledictionary/setobject%28_,forkey%29.md)
- [`removeObject(forKey:)`](./nsmutabledictionary/removeobject%28forkey%29.md)

You must also override the primitive methods of the [`NSDictionary`](./nsdictionary.md) class.

## Topics

### Creating and Initializing a Mutable Dictionary
- [init(capacity: Int)](./nsmutabledictionary/init%28capacity%29.md)
  Initializes a newly allocated mutable dictionary, allocating enough memory to hold `numItems` entries.
- [init()](./nsmutabledictionary/init%28%29.md)
  Initializes a newly allocated mutable dictionary.
- [init(sharedKeySet: Any)](./nsmutabledictionary/init%28sharedkeyset%29.md)
  Creates a mutable dictionary which is optimized for dealing with a known set of keys.
- [+ dictionaryWithCapacity:](./nsmutabledictionary/dictionarywithcapacity_.md)
  Creates and returns a mutable dictionary, initially giving it enough allocated memory to hold a given number of entries.
### Adding Entries to a Mutable Dictionary
- [func setObject(Any, forKey: any NSCopying)](./nsmutabledictionary/setobject%28_,forkey%29.md)
  Adds a given key-value pair to the dictionary.
- [func setValue(Any?, forKey: String)](./nsmutabledictionary/setvalue%28_,forkey%29.md)
  Adds a given key-value pair to the dictionary.
- [func addEntries(from: [AnyHashable : Any])](./nsmutabledictionary/addentries%28from%29.md)
  Adds to the receiving dictionary the entries from another dictionary.
- [func setDictionary([AnyHashable : Any])](./nsmutabledictionary/setdictionary%28_%29.md)
  Sets the contents of the receiving dictionary to entries in a given dictionary.
- [- setObject:forKeyedSubscript:](./nsmutabledictionary/setobject_forkeyedsubscript_.md)
  Adds a given key-value pair to the dictionary.
### Removing Entries From a Mutable Dictionary
- [func removeObject(forKey: Any)](./nsmutabledictionary/removeobject%28forkey%29.md)
  Removes a given key and its associated value from the dictionary.
- [func removeAllObjects()](./nsmutabledictionary/removeallobjects%28%29.md)
  Empties the dictionary of its entries.
- [func removeObjects(forKeys: [Any])](./nsmutabledictionary/removeobjects%28forkeys%29.md)
  Removes from the dictionary entries specified by elements in a given array.
### Initializers
- [convenience init!(OBEXHeadersData: Data!)](./nsmutabledictionary/init%28obexheadersdata%29.md)
- [convenience init!(OBEXHeadersData: UnsafeRawPointer!, headersDataSize: Int)](./nsmutabledictionary/init%28obexheadersdata,headersdatasize%29.md)
- [init?(coder: NSCoder)](./nsmutabledictionary/init%28coder%29.md)
### Instance Methods
- [func addApplicationParameterHeader(UnsafeRawPointer!, length: UInt32) -> OBEXError](./nsmutabledictionary/addapplicationparameterheader%28_,length%29.md)
- [func addAuthorizationChallengeHeader(UnsafeRawPointer!, length: UInt32) -> OBEXError](./nsmutabledictionary/addauthorizationchallengeheader%28_,length%29.md)
- [func addAuthorizationResponseHeader(UnsafeRawPointer!, length: UInt32) -> OBEXError](./nsmutabledictionary/addauthorizationresponseheader%28_,length%29.md)
- [func addBodyHeader(UnsafeRawPointer!, length: UInt32, endOfBody: Bool) -> OBEXError](./nsmutabledictionary/addbodyheader%28_,length,endofbody%29.md)
- [func addByteSequenceHeader(UnsafeRawPointer!, length: UInt32) -> OBEXError](./nsmutabledictionary/addbytesequenceheader%28_,length%29.md)
- [func addConnectionIDHeader(UnsafeRawPointer!, length: UInt32) -> OBEXError](./nsmutabledictionary/addconnectionidheader%28_,length%29.md)
- [func addCountHeader(UInt32) -> OBEXError](./nsmutabledictionary/addcountheader%28_%29.md)
- [func addDescriptionHeader(String!) -> OBEXError](./nsmutabledictionary/adddescriptionheader%28_%29.md)
- [func addHTTPHeader(UnsafeRawPointer!, length: UInt32) -> OBEXError](./nsmutabledictionary/addhttpheader%28_,length%29.md)
- [func addImageDescriptorHeader(UnsafeRawPointer!, length: UInt32) -> OBEXError](./nsmutabledictionary/addimagedescriptorheader%28_,length%29.md)
- [func addImageHandleHeader(String!) -> OBEXError](./nsmutabledictionary/addimagehandleheader%28_%29.md)
- [func addLengthHeader(UInt32) -> OBEXError](./nsmutabledictionary/addlengthheader%28_%29.md)
- [func addNameHeader(String!) -> OBEXError](./nsmutabledictionary/addnameheader%28_%29.md)
- [func addObjectClassHeader(UnsafeRawPointer!, length: UInt32) -> OBEXError](./nsmutabledictionary/addobjectclassheader%28_,length%29.md)
- [func addTargetHeader(UnsafeRawPointer!, length: UInt32) -> OBEXError](./nsmutabledictionary/addtargetheader%28_,length%29.md)
- [func addTime4ByteHeader(UInt32) -> OBEXError](./nsmutabledictionary/addtime4byteheader%28_%29.md)
- [func addTimeISOHeader(UnsafeRawPointer!, length: UInt32) -> OBEXError](./nsmutabledictionary/addtimeisoheader%28_,length%29.md)
- [func addTypeHeader(String!) -> OBEXError](./nsmutabledictionary/addtypeheader%28_%29.md)
- [func addUserDefinedHeader(UnsafeRawPointer!, length: UInt32) -> OBEXError](./nsmutabledictionary/adduserdefinedheader%28_,length%29.md)
- [func addWhoHeader(UnsafeRawPointer!, length: UInt32) -> OBEXError](./nsmutabledictionary/addwhoheader%28_,length%29.md)
- [func getHeaderBytes() -> NSMutableData!](./nsmutabledictionary/getheaderbytes%28%29.md)
- [- initWithContentsOfFile:](./nsmutabledictionary/initwithcontentsoffile_.md)
- [- initWithContentsOfURL:](./nsmutabledictionary/initwithcontentsofurl_.md)
### Default Implementations
- [NSDictionary Implementations](./nsmutabledictionary/nsdictionary-implementations.md)
- [NSMutableDictionary Implementations](./nsmutabledictionary/nsmutabledictionary-implementations.md)
### Type Methods
- [+ dictionaryWithContentsOfFile:](./nsmutabledictionary/dictionarywithcontentsoffile_.md)
- [+ dictionaryWithContentsOfURL:](./nsmutabledictionary/dictionarywithcontentsofurl_.md)
- [+ withOBEXHeadersData:headersDataSize:](./nsmutabledictionary/withobexheadersdata_headersdatasize_.md)

## Relationships

### Inherits From
- [NSDictionary](./nsdictionary.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomReflectable](../Swift/customreflectable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByDictionaryLiteral](../Swift/expressiblebydictionaryliteral.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](./nscoding.md)
- [NSCopying](./nscopying.md)
- [NSFastEnumeration](./nsfastenumeration.md)
- [NSMutableCopying](./nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](./nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [Sequence](../Swift/sequence.md)

## See Also

### Basic Collections
- [NSArray](./nsarray.md)
  A static ordered collection of objects.
- [NSMutableArray](./nsmutablearray.md)
  A dynamic ordered collection of objects.
- [NSDictionary](./nsdictionary.md)
  A static collection of objects associated with unique keys.
- [NSSet](./nsset.md)
  A static, unordered collection of unique objects.
- [NSMutableSet](./nsmutableset.md)
  A dynamic unordered collection of unique objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutabledictionary)*