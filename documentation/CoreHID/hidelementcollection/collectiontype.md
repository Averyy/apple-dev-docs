# HIDElementCollection.CollectionType

**Framework**: Core HID  
**Kind**: enum

Types of [`HIDElementCollection`](hidelementcollection.md)s.

**Availability**:
- macOS 15.0+

## Declaration

```swift
enum CollectionType
```

#### Overview

Collection types are a defined part of the HID specification that define how a collection is intended to be used.

See the HID specification for more details: [`https://www.usb.org/hid`](https://developer.apple.comhttps://www.usb.org/hid).

## Topics

### Operators
- [static func == (HIDElementCollection.CollectionType, HIDElementCollection.CollectionType) -> Bool](hidelementcollection/collectiontype/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [HIDElementCollection.CollectionType.application](hidelementcollection/collectiontype/application.md)
- [HIDElementCollection.CollectionType.logical](hidelementcollection/collectiontype/logical.md)
- [HIDElementCollection.CollectionType.namedArray](hidelementcollection/collectiontype/namedarray.md)
- [HIDElementCollection.CollectionType.physical](hidelementcollection/collectiontype/physical.md)
- [HIDElementCollection.CollectionType.report](hidelementcollection/collectiontype/report.md)
- [HIDElementCollection.CollectionType.usageModifier](hidelementcollection/collectiontype/usagemodifier.md)
- [HIDElementCollection.CollectionType.usageSwitch](hidelementcollection/collectiontype/usageswitch.md)
### Instance Properties
- [var hashValue: Int](hidelementcollection/collectiontype/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](hidelementcollection/collectiontype/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](hidelementcollection/collectiontype/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidelementcollection/collectiontype)*