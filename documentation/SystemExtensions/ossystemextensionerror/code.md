# OSSystemExtensionError.Code

**Framework**: System Extensions  
**Kind**: enum

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

## Topics

### Error Codes
- [OSSystemExtensionError.Code.unknown](ossystemextensionerror/code/unknown.md)
  An error code that indicates an unknown error occurred.
- [OSSystemExtensionError.Code.missingEntitlement](ossystemextensionerror/code/missingentitlement.md)
  An error code that indicates the system extension lacks a required entitlement.
- [OSSystemExtensionError.Code.unsupportedParentBundleLocation](ossystemextensionerror/code/unsupportedparentbundlelocation.md)
  An error code that indicates the extension’s parent app isn’t in a valid location for activation.
- [OSSystemExtensionError.Code.extensionNotFound](ossystemextensionerror/code/extensionnotfound.md)
  An error code that indicates the manager can’t find the system extension.
- [OSSystemExtensionError.Code.extensionMissingIdentifier](ossystemextensionerror/code/extensionmissingidentifier.md)
  An error code that indicates the extension identifier is missing.
- [OSSystemExtensionError.Code.duplicateExtensionIdentifer](ossystemextensionerror/code/duplicateextensionidentifer.md)
  An error code that indicates the extension identifier duplicates an existing identifier.
- [OSSystemExtensionError.Code.unknownExtensionCategory](ossystemextensionerror/code/unknownextensioncategory.md)
  An error code that indicates the extension manager can’t recognize the extension’s category identifier.
- [OSSystemExtensionError.Code.codeSignatureInvalid](ossystemextensionerror/code/codesignatureinvalid.md)
  An error code that indicates the extension’s signature is invalid.
- [OSSystemExtensionError.Code.validationFailed](ossystemextensionerror/code/validationfailed.md)
  An error code that indicates the manager can’t validate the extension.
- [OSSystemExtensionError.Code.forbiddenBySystemPolicy](ossystemextensionerror/code/forbiddenbysystempolicy.md)
  An error code that indicates the system policy prohibits activating the system extension.
- [OSSystemExtensionError.Code.requestCanceled](ossystemextensionerror/code/requestcanceled.md)
  An error code that indicates the system extension manager request was canceled.
- [OSSystemExtensionError.Code.requestSuperseded](ossystemextensionerror/code/requestsuperseded.md)
  An error code that indicates the system extension request failed because the system already has a pending request for the same identifier.
- [OSSystemExtensionError.Code.authorizationRequired](ossystemextensionerror/code/authorizationrequired.md)
  An error code that indicates the system was unable to obtain the proper authorization.
### Initializers
- [init?(rawValue: Int)](ossystemextensionerror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct OSSystemExtensionError](ossystemextensionerror.md)
  An error that describes a failed extension manager request.
- [let OSSystemExtensionErrorDomain: String](ossystemextensionerrordomain.md)
  The error domain identifying system extension errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemextensions/ossystemextensionerror/code)*