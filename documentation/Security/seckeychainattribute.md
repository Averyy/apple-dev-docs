# SecKeychainAttribute

**Framework**: Security  
**Kind**: struct

A structure that holds a single keychain attribute.

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct SecKeychainAttribute
```

## Topics

### Instance Properties
- [var data: UnsafeMutableRawPointer?](seckeychainattribute/data.md)
  A pointer to the attribute data.
- [var length: UInt32](seckeychainattribute/length.md)
  The length of the buffer pointed to by data.
- [var tag: SecKeychainAttrType](seckeychainattribute/tag.md)
  A 4-byte attribute tag.
### Initializers
- [init()](seckeychainattribute/init.md)
- [init(tag: SecKeychainAttrType, length: UInt32, data: UnsafeMutableRawPointer?)](seckeychainattribute/init(tag:length:data:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainattribute)*