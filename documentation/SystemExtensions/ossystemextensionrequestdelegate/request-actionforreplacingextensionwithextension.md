# request(_:actionForReplacingExtension:withExtension:)

**Framework**: System Extensions  
**Kind**: method  
**Required**: Yes

Tells the delegate that the user has a different version of the extension installed on their system.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func request(_ request: OSSystemExtensionRequest, actionForReplacingExtension existing: OSSystemExtensionProperties, withExtension ext: OSSystemExtensionProperties) -> OSSystemExtensionRequest.ReplacementAction
```

## Mentions

- [Installing System Extensions and Drivers](installing-system-extensions-and-drivers.md)

#### Return Value

A replacement action the manager should take to resolve the conflict.

#### Discussion

The manager calls this method when it encounters an existing extension with the same team and bundle identifiers, but with different version identifiers. It uses the [`CFBundleVersion`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleVersion) and [`CFBundleShortVersionString`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleShortVersionString) identifiers to determine if the existing and new versions differ. The delegate must make a decision on whether to replace the existing extension.

Implement this method to return an [`OSSystemExtensionRequest.ReplacementAction`](ossystemextensionrequest/replacementaction.md), which tells the manager what to do. If you return [`OSSystemExtensionRequest.ReplacementAction.cancel`](ossystemextensionrequest/replacementaction/cancel.md), the manager aborts the installation and calls [`request(_:didFailWithError:)`](ossystemextensionrequestdelegate/request(_:didfailwitherror:).md), with the [`OSSystemExtensionError.Code.requestCanceled`](ossystemextensionerror/code/requestcanceled.md) error code.

If the local system has System Extension developer mode enabled, the manager always calls this method when it finds an existing installation, even if the version identifiers match.

## Parameters

- `request`: The request that encountered a conflict.
- `existing`: A properties object that describes the installed version of the extension.
- `ext`: A properties object that describes the updated version of the extension.

## See Also

- [func requestNeedsUserApproval(OSSystemExtensionRequest)](ossystemextensionrequestdelegate/requestneedsuserapproval(_:).md)
  Tells the delegate that the user must grant approval before the manager can activate the extension.
- [class OSSystemExtensionProperties](ossystemextensionproperties.md)
  Properties that identify a specific version of a system extension.
- [OSSystemExtensionRequest.ReplacementAction](ossystemextensionrequest/replacementaction.md)
  Actions for describing how the extension manager should resolve a version conflict.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemextensions/ossystemextensionrequestdelegate/request(_:actionforreplacingextension:withextension:))*