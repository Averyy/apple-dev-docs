# ASCredentialIdentityStoreError.Code

**Framework**: Authentication Services  
**Kind**: enum  
**Role**: Enumeration

Constants that represent credential identity store error codes.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

```c
enum ASCredentialIdentityStoreErrorCode : NSInteger;
```

## Topics

### Codes
- [ASCredentialIdentityStoreError.Code.internalError](./code/internalerror.md)
  The operation failed due to an internal error.
- [ASCredentialIdentityStoreError.Code.storeBusy](./code/storebusy.md)
  The operation failed because the credential identity store is busy.
- [ASCredentialIdentityStoreError.Code.storeDisabled](./code/storedisabled.md)
  The operation failed because the credential identity store is disabled.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Recognizing errors
- [struct ASCredentialIdentityStoreError](../ascredentialidentitystoreerror.md)
  A credential identity store error.
- [let ASCredentialIdentityStoreErrorDomain: String](../ascredentialidentitystoreerrordomain.md)
  The domain for a credential identity store error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialidentitystoreerror/code)*