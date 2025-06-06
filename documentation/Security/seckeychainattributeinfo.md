# SecKeychainAttributeInfo

**Framework**: Security  
**Kind**: struct

A structure that represents an attribute.

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct SecKeychainAttributeInfo
```

#### Overview

Each tag and format item form a pair. Use [`SecKeychainAttributeInfoForItemID(_:_:_:)`](seckeychainattributeinfoforitemid(_:_:_:).md) to obtain the structure for a given keychain item, and [`SecKeychainFreeAttributeInfo(_:)`](seckeychainfreeattributeinfo(_:).md) to release that structure’s memory when you are done with it. Use an instance of this structure in a call to the [`SecKeychainItemCopyAttributesAndData(_:_:_:_:_:_:)`](seckeychainitemcopyattributesanddata(_:_:_:_:_:_:).md) function to specify the attributes of a keychain item to retrieve.

## Topics

### Instance Properties
- [var count: UInt32](seckeychainattributeinfo/count.md)
  The number of tag-format pairs in the respective arrays.
- [var format: UnsafeMutablePointer<UInt32>?](seckeychainattributeinfo/format.md)
  A pointer to the first attribute format in the array.
- [var tag: UnsafeMutablePointer<UInt32>](seckeychainattributeinfo/tag.md)
  A pointer to the first attribute tag in the array.
### Initializers
- [init(count: UInt32, tag: UnsafeMutablePointer<UInt32>, format: UnsafeMutablePointer<UInt32>?)](seckeychainattributeinfo/init(count:tag:format:).md)
  Creates a new attribute information structure.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainattributeinfo)*