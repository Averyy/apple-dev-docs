# SecKeychainAttributeList

**Framework**: Security  
**Kind**: struct

A list of keychain attributes.

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct SecKeychainAttributeList
```

## Topics

### Instance Properties
- [var attr: UnsafeMutablePointer<SecKeychainAttribute>?](seckeychainattributelist/attr.md)
  A pointer to the first keychain attribute in the array.
- [var count: UInt32](seckeychainattributelist/count.md)
  The number of keychain attributes in the array.
### Initializers
- [init()](seckeychainattributelist/init.md)
- [init(count: UInt32, attr: UnsafeMutablePointer<SecKeychainAttribute>?)](seckeychainattributelist/init(count:attr:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainattributelist)*