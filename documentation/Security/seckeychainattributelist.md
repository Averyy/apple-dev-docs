# SecKeychainAttributeList

**Framework**: Security  
**Kind**: struct  
**Role**: Structure

A list of keychain attributes.

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct SecKeychainAttributeList
```

```c
struct SecKeychainAttributeList;
```

## Topics

### Instance Properties
- [var attr: UnsafeMutablePointer<SecKeychainAttribute>?](./seckeychainattributelist/attr.md)
  A pointer to the first keychain attribute in the array.
- [var count: UInt32](./seckeychainattributelist/count.md)
  The number of keychain attributes in the array.
### Initializers
- [init()](./seckeychainattributelist/init%28%29.md)
- [init(count: UInt32, attr: UnsafeMutablePointer<SecKeychainAttribute>?)](./seckeychainattributelist/init%28count,attr%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainattributelist)*