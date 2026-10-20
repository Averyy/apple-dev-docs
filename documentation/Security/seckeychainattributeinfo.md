# SecKeychainAttributeInfo

**Framework**: Security  
**Kind**: struct  
**Role**: Structure

A structure that represents an attribute.

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct SecKeychainAttributeInfo
```

```c
struct SecKeychainAttributeInfo;
```

#### Overview

Each tag and format item form a pair. Use [`SecKeychainAttributeInfoForItemID(_:_:_:)`](./seckeychainattributeinfoforitemid%28_,_,_%29.md) to obtain the structure for a given keychain item, and [`SecKeychainFreeAttributeInfo(_:)`](./seckeychainfreeattributeinfo%28_%29.md) to release that structure’s memory when you are done with it. Use an instance of this structure in a call to the [`SecKeychainItemCopyAttributesAndData(_:_:_:_:_:_:)`](./seckeychainitemcopyattributesanddata%28_,_,_,_,_,_%29.md) function to specify the attributes of a keychain item to retrieve.

## Topics

### Instance Properties
- [var count: UInt32](./seckeychainattributeinfo/count.md)
  The number of tag-format pairs in the respective arrays.
- [var format: UnsafeMutablePointer<UInt32>?](./seckeychainattributeinfo/format.md)
  A pointer to the first attribute format in the array.
- [var tag: UnsafeMutablePointer<UInt32>](./seckeychainattributeinfo/tag.md)
  A pointer to the first attribute tag in the array.
### Initializers
- [init(count: UInt32, tag: UnsafeMutablePointer<UInt32>, format: UnsafeMutablePointer<UInt32>?)](./seckeychainattributeinfo/init%28count,tag,format%29.md)
  Creates a new attribute information structure.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainattributeinfo)*