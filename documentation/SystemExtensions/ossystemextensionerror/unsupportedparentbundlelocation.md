# unsupportedParentBundleLocation

**Framework**: System Extensions  
**Kind**: property  
**Role**: Type Property

An error code that indicates the extension’s parent app isn’t in a valid location for activation.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 10.15+

## Declaration

```swift
static var unsupportedParentBundleLocation: OSSystemExtensionError.Code { get }
```

#### Discussion

The expected location of a driver extension is in the `Contents/Library/SystemExtensions` directory of a macOS app. The app itself must be in one of the system’s `Applications` directories.

## See Also

### Error Codes
- [OSSystemExtensionError.Code](./code.md)
  Error codes for system extensions.
- [static var unknown: OSSystemExtensionError.Code](./unknown.md)
  An error code that indicates an unknown error occurred.
- [static var missingEntitlement: OSSystemExtensionError.Code](./missingentitlement.md)
  An error code that indicates the system extension lacks a required entitlement.
- [static var extensionNotFound: OSSystemExtensionError.Code](./extensionnotfound.md)
  An error code that indicates the manager can’t find the system extension.
- [static var extensionMissingIdentifier: OSSystemExtensionError.Code](./extensionmissingidentifier.md)
  An error code that indicates the extension identifier is missing.
- [static var duplicateExtensionIdentifer: OSSystemExtensionError.Code](./duplicateextensionidentifer.md)
  An error code that indicates the extension identifier duplicates an existing identifier.
- [static var unknownExtensionCategory: OSSystemExtensionError.Code](./unknownextensioncategory.md)
  An error code that indicates the extension manager can’t recognize the extension’s category identifier.
- [static var codeSignatureInvalid: OSSystemExtensionError.Code](./codesignatureinvalid.md)
  An error code that indicates the extension’s signature is invalid.
- [static var validationFailed: OSSystemExtensionError.Code](./validationfailed.md)
  An error code that indicates the manager can’t validate the extension.
- [static var forbiddenBySystemPolicy: OSSystemExtensionError.Code](./forbiddenbysystempolicy.md)
  An error code that indicates the system policy prohibits activating the system extension.
- [static var requestCanceled: OSSystemExtensionError.Code](./requestcanceled.md)
  An error code that indicates the system extension manager request was canceled.
- [static var requestSuperseded: OSSystemExtensionError.Code](./requestsuperseded.md)
  An error code that indicates the system extension request failed because the system already has a pending request for the same identifier.
- [static var authorizationRequired: OSSystemExtensionError.Code](./authorizationrequired.md)
  An error code that indicates the system was unable to obtain the proper authorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemextensions/ossystemextensionerror/unsupportedparentbundlelocation)*