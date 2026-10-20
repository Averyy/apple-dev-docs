# SecKeychainAttribute

**Framework**: Security  
**Kind**: struct  
**Role**: Structure

A structure that holds a single keychain attribute.

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct SecKeychainAttribute
```

```c
struct SecKeychainAttribute;
```

## Topics

### Instance Properties
- [var data: UnsafeMutableRawPointer?](./seckeychainattribute/data.md)
  A pointer to the attribute data.
- [var length: UInt32](./seckeychainattribute/length.md)
  The length of the buffer pointed to by data.
- [var tag: SecKeychainAttrType](./seckeychainattribute/tag.md)
  A 4-byte attribute tag.
### Initializers
- [init()](./seckeychainattribute/init%28%29.md)
- [init(tag: SecKeychainAttrType, length: UInt32, data: UnsafeMutableRawPointer?)](./seckeychainattribute/init%28tag,length,data%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainattribute)*