# ASError.Code

**Framework**: AccessorySetupKit  
**Kind**: enum  
**Role**: Enumeration

Codes that describe errors encountered during accessory discovery.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
enum Code
```

```c
enum ASErrorCode : NSInteger;
```

## Topics

### Activation errors
- [ASError.Code.activationFailed](./code/activationfailed.md)
  Session activation failed.
### Timeout and life cycle errors
- [ASError.Code.discoveryTimeout](./code/discoverytimeout.md)
  Accessory discovery timed out.
- [ASError.Code.invalidated](./code/invalidated.md)
  The session invalidated prior to completing the operation.
### Configuration errors
- [ASError.Code.extensionNotFound](./code/extensionnotfound.md)
  The framework couldn’t find the app extension.
- [ASError.Code.userRestricted](./code/userrestricted.md)
  The person using the app restricted access.
- [ASError.Code.invalidRequest](./code/invalidrequest.md)
  The session received an invalid request.
### Picker errors
- [ASError.Code.pickerRestricted](./code/pickerrestricted.md)
  The picker can’t be used because the app is in the background.
- [ASError.Code.pickerAlreadyActive](./code/pickeralreadyactive.md)
  The picker received a show request when it was already active.
### Cancellation errors
- [ASError.Code.userCancelled](./code/usercancelled.md)
  The person using the app canceled the operation.
### Communication errors
- [ASError.Code.connectionFailed](./code/connectionfailed.md)
  The session was unable to establish a connection.
### Success cases
- [ASError.Code.success](./code/success.md)
  A code that represents a successful action.
### Unclassified errors
- [ASError.Code.unknown](./code/unknown.md)
  An underlying failure with an unknown cause.
### Accessing the error domain
- [static var errorDomain: String](./errordomain.md)
- [let ASErrorDomain: String](../aserrordomain.md)
  NSError domain for AccessorySetupKit errors.
### Working with raw values
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

### Errors
- [struct ASError](../aserror.md)
  An error encountered during accessory discovery.
- [let ASErrorDomain: String](../aserrordomain.md)
  NSError domain for AccessorySetupKit errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/aserror/code)*