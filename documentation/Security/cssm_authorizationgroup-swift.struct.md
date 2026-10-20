# cssm_authorizationgroup

**Framework**: Security  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct cssm_authorizationgroup
```

```c
struct cssm_authorizationgroup;
```

## Topics

### Initializers
- [init()](./cssm_authorizationgroup-swift.struct/init%28%29.md)
- [init(NumberOfAuthTags: uint32, AuthTags: UnsafeMutablePointer<CSSM_ACL_AUTHORIZATION_TAG>!)](./cssm_authorizationgroup-swift.struct/init%28numberofauthtags,authtags%29.md)
### Instance Properties
- [var AuthTags: UnsafeMutablePointer<CSSM_ACL_AUTHORIZATION_TAG>!](./cssm_authorizationgroup-swift.struct/authtags.md)
- [var NumberOfAuthTags: uint32](./cssm_authorizationgroup-swift.struct/numberofauthtags.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_authorizationgroup-swift.struct)*