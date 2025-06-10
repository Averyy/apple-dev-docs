# NSMutableDictionary

**Framework**: Foundation  
**Kind**: class

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

#### Overview

In Swift, you can use this type instead of a [`Dictionary`](https://developer.apple.com/documentation/Swift/Dictionary) variable in cases that require reference semantics.

The `NSMutableDictionary` class declares the programmatic interface to objects that manage mutable associations of keys and values. It adds modification operations to the basic operations it inherits from [`NSDictionary`](nsdictionary.md).

`NSMutableDictionary` is “toll-free bridged” with its Core Foundation counterpart, [`CFMutableDictionary`](https://developer.apple.com/documentation/CoreFoundation/CFMutableDictionary). See [`Toll-Free Bridging`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information on toll-free bridging.

##### Setting Values Using Subscripting

In addition to the provided instance methods, such as [`setObject(_:forKey:)`](nsmutabledictionary/setobject(_:forkey:).md), you can access `NSDictionary` values by their keys using .

##### Subclassing Notes

There should typically be little need to subclass `NSMutableDictionary`. If you do need to customize behavior, it is often better to consider composition rather than subclassing.

###### Methods to Override

In a subclass, you must override both of its primitive methods:

- [`setObject(_:forKey:)`](nsmutabledictionary/setobject(_:forkey:).md)
- [`removeObject(forKey:)`](nsmutabledictionary/removeobject(forkey:).md)

You must also override the primitive methods of the [`NSDictionary`](nsdictionary.md) class.

## Topics

### Creating and Initializing a Mutable Dictionary
- [init(capacity: Int)](nsmutabledictionary/init(capacity:).md)
  Initializes a newly allocated mutable dictionary, allocating enough memory to hold `numItems` entries.
- [init()](nsmutabledictionary/init.md)
  Initializes a newly allocated mutable dictionary.
- [init(sharedKeySet: Any)](nsmutabledictionary/init(sharedkeyset:).md)
  Creates a mutable dictionary which is optimized for dealing with a known set of keys.
### Adding Entries to a Mutable Dictionary
- [func setObject(Any, forKey: any NSCopying)](nsmutabledictionary/setobject(_:forkey:).md)
  Adds a given key-value pair to the dictionary.
- [func setValue(Any?, forKey: String)](nsmutabledictionary/setvalue(_:forkey:).md)
  Adds a given key-value pair to the dictionary.
- [func addEntries(from: [AnyHashable : Any])](nsmutabledictionary/addentries(from:).md)
  Adds to the receiving dictionary the entries from another dictionary.
- [func setDictionary([AnyHashable : Any])](nsmutabledictionary/setdictionary(_:).md)
  Sets the contents of the receiving dictionary to entries in a given dictionary.
### Removing Entries From a Mutable Dictionary
- [func removeObject(forKey: Any)](nsmutabledictionary/removeobject(forkey:).md)
  Removes a given key and its associated value from the dictionary.
- [func removeAllObjects()](nsmutabledictionary/removeallobjects.md)
  Empties the dictionary of its entries.
- [func removeObjects(forKeys: [Any])](nsmutabledictionary/removeobjects(forkeys:).md)
  Removes from the dictionary entries specified by elements in a given array.
### Initializers
- [convenience init!(OBEXHeadersData: Data!)](nsmutabledictionary/init(obexheadersdata:).md)
- [convenience init!(OBEXHeadersData: UnsafeRawPointer!, headersDataSize: Int)](nsmutabledictionary/init(obexheadersdata:headersdatasize:).md)
- [init?(coder: NSCoder)](nsmutabledictionary/init(coder:).md)
- [init?(contentsOfURL: URL)](nsmutabledictionary/init(contentsofurl:).md)
### Instance Methods
- [func addApplicationParameterHeader(UnsafeRawPointer!, length: UInt32) -> OBEXError](nsmutabledictionary/addapplicationparameterheader(_:length:).md)
- [func addAuthorizationChallengeHeader(UnsafeRawPointer!, length: UInt32) -> OBEXError](nsmutabledictionary/addauthorizationchallengeheader(_:length:).md)
- [func addAuthorizationResponseHeader(UnsafeRawPointer!, length: UInt32) -> OBEXError](nsmutabledictionary/addauthorizationresponseheader(_:length:).md)
- [func addBodyHeader(UnsafeRawPointer!, length: UInt32, endOfBody: Bool) -> OBEXError](nsmutabledictionary/addbodyheader(_:length:endofbody:).md)
- [func addByteSequenceHeader(UnsafeRawPointer!, length: UInt32) -> OBEXError](nsmutabledictionary/addbytesequenceheader(_:length:).md)
- [func addConnectionIDHeader(UnsafeRawPointer!, length: UInt32) -> OBEXError](nsmutabledictionary/addconnectionidheader(_:length:).md)
- [func addCountHeader(UInt32) -> OBEXError](nsmutabledictionary/addcountheader(_:).md)
- [func addDescriptionHeader(String!) -> OBEXError](nsmutabledictionary/adddescriptionheader(_:).md)
- [func addHTTPHeader(UnsafeRawPointer!, length: UInt32) -> OBEXError](nsmutabledictionary/addhttpheader(_:length:).md)
- [func addImageDescriptorHeader(UnsafeRawPointer!, length: UInt32) -> OBEXError](nsmutabledictionary/addimagedescriptorheader(_:length:).md)
- [func addImageHandleHeader(String!) -> OBEXError](nsmutabledictionary/addimagehandleheader(_:).md)
- [func addLengthHeader(UInt32) -> OBEXError](nsmutabledictionary/addlengthheader(_:).md)
- [func addNameHeader(String!) -> OBEXError](nsmutabledictionary/addnameheader(_:).md)
- [func addObjectClassHeader(UnsafeRawPointer!, length: UInt32) -> OBEXError](nsmutabledictionary/addobjectclassheader(_:length:).md)
- [func addTargetHeader(UnsafeRawPointer!, length: UInt32) -> OBEXError](nsmutabledictionary/addtargetheader(_:length:).md)
- [func addTime4ByteHeader(UInt32) -> OBEXError](nsmutabledictionary/addtime4byteheader(_:).md)
- [func addTimeISOHeader(UnsafeRawPointer!, length: UInt32) -> OBEXError](nsmutabledictionary/addtimeisoheader(_:length:).md)
- [func addTypeHeader(String!) -> OBEXError](nsmutabledictionary/addtypeheader(_:).md)
- [func addUserDefinedHeader(UnsafeRawPointer!, length: UInt32) -> OBEXError](nsmutabledictionary/adduserdefinedheader(_:length:).md)
- [func addWhoHeader(UnsafeRawPointer!, length: UInt32) -> OBEXError](nsmutabledictionary/addwhoheader(_:length:).md)
- [func getHeaderBytes() -> NSMutableData!](nsmutabledictionary/getheaderbytes.md)
### Subscripts
- [subscript(Any) -> Any?](nsmutabledictionary/subscript(_:).md)

## Relationships

### Inherits From
- [NSDictionary](nsdictionary.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByDictionaryLiteral](../Swift/ExpressibleByDictionaryLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSFastEnumeration](nsfastenumeration.md)
- [NSMutableCopying](nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Sequence](../Swift/Sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutabledictionary)*