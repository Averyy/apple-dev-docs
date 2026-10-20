# OSSystemExtensionError.Code

**Framework**: System Extensions  
**Kind**: enum  
**Role**: Enumeration

Error codes for system extensions.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 10.15+

## Declaration

```swift
enum Code
```

```c
enum OSSystemExtensionErrorCode : NSInteger;
```

## Topics

### Error Codes
- [OSSystemExtensionError.Code.unknown](./code/unknown.md)
  An error code that indicates an unknown error occurred.
- [OSSystemExtensionError.Code.missingEntitlement](./code/missingentitlement.md)
  An error code that indicates the system extension lacks a required entitlement.
- [OSSystemExtensionError.Code.unsupportedParentBundleLocation](./code/unsupportedparentbundlelocation.md)
  An error code that indicates the extension’s parent app isn’t in a valid location for activation.
- [OSSystemExtensionError.Code.extensionNotFound](./code/extensionnotfound.md)
  An error code that indicates the manager can’t find the system extension.
- [OSSystemExtensionError.Code.extensionMissingIdentifier](./code/extensionmissingidentifier.md)
  An error code that indicates the extension identifier is missing.
- [OSSystemExtensionError.Code.duplicateExtensionIdentifer](./code/duplicateextensionidentifer.md)
  An error code that indicates the extension identifier duplicates an existing identifier.
- [OSSystemExtensionError.Code.unknownExtensionCategory](./code/unknownextensioncategory.md)
  An error code that indicates the extension manager can’t recognize the extension’s category identifier.
- [OSSystemExtensionError.Code.codeSignatureInvalid](./code/codesignatureinvalid.md)
  An error code that indicates the extension’s signature is invalid.
- [OSSystemExtensionError.Code.validationFailed](./code/validationfailed.md)
  An error code that indicates the manager can’t validate the extension.
- [OSSystemExtensionError.Code.forbiddenBySystemPolicy](./code/forbiddenbysystempolicy.md)
  An error code that indicates the system policy prohibits activating the system extension.
- [OSSystemExtensionError.Code.requestCanceled](./code/requestcanceled.md)
  An error code that indicates the system extension manager request was canceled.
- [OSSystemExtensionError.Code.requestSuperseded](./code/requestsuperseded.md)
  An error code that indicates the system extension request failed because the system already has a pending request for the same identifier.
- [OSSystemExtensionError.Code.authorizationRequired](./code/authorizationrequired.md)
  An error code that indicates the system was unable to obtain the proper authorization.
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

### Errors
- [struct OSSystemExtensionError](../ossystemextensionerror.md)
  An error that describes a failed extension manager request.
- [let OSSystemExtensionErrorDomain: String](../ossystemextensionerrordomain.md)
  The error domain identifying system extension errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemextensions/ossystemextensionerror/code)*