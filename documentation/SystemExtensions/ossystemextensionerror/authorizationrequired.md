# authorizationRequired

**Framework**: System Extensions  
**Kind**: property

An error code that indicates the system was unable to obtain the proper authorization.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 10.15+

## Declaration

```swift
static var authorizationRequired: OSSystemExtensionError.Code { get }
```

## See Also

- [OSSystemExtensionError.Code](ossystemextensionerror/code.md)
  Error codes for system extensions.
- [static var unknown: OSSystemExtensionError.Code](ossystemextensionerror/unknown.md)
  An error code that indicates an unknown error occurred.
- [static var missingEntitlement: OSSystemExtensionError.Code](ossystemextensionerror/missingentitlement.md)
  An error code that indicates the system extension lacks a required entitlement.
- [static var unsupportedParentBundleLocation: OSSystemExtensionError.Code](ossystemextensionerror/unsupportedparentbundlelocation.md)
  An error code that indicates the extension’s parent app isn’t in a valid location for activation.
- [static var extensionNotFound: OSSystemExtensionError.Code](ossystemextensionerror/extensionnotfound.md)
  An error code that indicates the manager can’t find the system extension.
- [static var extensionMissingIdentifier: OSSystemExtensionError.Code](ossystemextensionerror/extensionmissingidentifier.md)
  An error code that indicates the extension identifier is missing.
- [static var duplicateExtensionIdentifer: OSSystemExtensionError.Code](ossystemextensionerror/duplicateextensionidentifer.md)
  An error code that indicates the extension identifier duplicates an existing identifier.
- [static var unknownExtensionCategory: OSSystemExtensionError.Code](ossystemextensionerror/unknownextensioncategory.md)
  An error code that indicates the extension manager can’t recognize the extension’s category identifier.
- [static var codeSignatureInvalid: OSSystemExtensionError.Code](ossystemextensionerror/codesignatureinvalid.md)
  An error code that indicates the extension’s signature is invalid.
- [static var validationFailed: OSSystemExtensionError.Code](ossystemextensionerror/validationfailed.md)
  An error code that indicates the manager can’t validate the extension.
- [static var forbiddenBySystemPolicy: OSSystemExtensionError.Code](ossystemextensionerror/forbiddenbysystempolicy.md)
  An error code that indicates the system policy prohibits activating the system extension.
- [static var requestCanceled: OSSystemExtensionError.Code](ossystemextensionerror/requestcanceled.md)
  An error code that indicates the system extension manager request was canceled.
- [static var requestSuperseded: OSSystemExtensionError.Code](ossystemextensionerror/requestsuperseded.md)
  An error code that indicates the system extension request failed because the system already has a pending request for the same identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemextensions/ossystemextensionerror/authorizationrequired)*