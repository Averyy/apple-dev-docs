# OSSystemExtensionError.Code.requestCanceled

**Framework**: System Extensions  
**Kind**: case  
**Role**: Case

An error code that indicates the system extension manager request was canceled.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 10.15+

## Declaration

```swift
case requestCanceled
```

```c
OSSystemExtensionErrorRequestCanceled
```

## See Also

### Error Codes
- [OSSystemExtensionError.Code.unknown](./unknown.md)
  An error code that indicates an unknown error occurred.
- [OSSystemExtensionError.Code.missingEntitlement](./missingentitlement.md)
  An error code that indicates the system extension lacks a required entitlement.
- [OSSystemExtensionError.Code.unsupportedParentBundleLocation](./unsupportedparentbundlelocation.md)
  An error code that indicates the extension’s parent app isn’t in a valid location for activation.
- [OSSystemExtensionError.Code.extensionNotFound](./extensionnotfound.md)
  An error code that indicates the manager can’t find the system extension.
- [OSSystemExtensionError.Code.extensionMissingIdentifier](./extensionmissingidentifier.md)
  An error code that indicates the extension identifier is missing.
- [OSSystemExtensionError.Code.duplicateExtensionIdentifer](./duplicateextensionidentifer.md)
  An error code that indicates the extension identifier duplicates an existing identifier.
- [OSSystemExtensionError.Code.unknownExtensionCategory](./unknownextensioncategory.md)
  An error code that indicates the extension manager can’t recognize the extension’s category identifier.
- [OSSystemExtensionError.Code.codeSignatureInvalid](./codesignatureinvalid.md)
  An error code that indicates the extension’s signature is invalid.
- [OSSystemExtensionError.Code.validationFailed](./validationfailed.md)
  An error code that indicates the manager can’t validate the extension.
- [OSSystemExtensionError.Code.forbiddenBySystemPolicy](./forbiddenbysystempolicy.md)
  An error code that indicates the system policy prohibits activating the system extension.
- [OSSystemExtensionError.Code.requestSuperseded](./requestsuperseded.md)
  An error code that indicates the system extension request failed because the system already has a pending request for the same identifier.
- [OSSystemExtensionError.Code.authorizationRequired](./authorizationrequired.md)
  An error code that indicates the system was unable to obtain the proper authorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemextensions/ossystemextensionerror/code/requestcanceled)*