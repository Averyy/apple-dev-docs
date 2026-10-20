# UIAccessibility.GuidedAccessError

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

A Guided Access error.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
struct GuidedAccessError
```

## Topics

### Accessing error codes
- [static var permissionDenied: UIAccessibility.GuidedAccessError.Code](./guidedaccesserror/permissiondenied.md)
  An error that indicates the app isn’t authorized to perform the requested action.
- [static var failed: UIAccessibility.GuidedAccessError.Code](./guidedaccesserror/failed.md)
  An error that indicates a failure for an unspecified reason.
- [UIAccessibility.GuidedAccessError.Code](./guidedaccesserror/code.md)
  Error codes for Guided Access.
### Getting error information
- [static var errorDomain: String](./guidedaccesserror/errordomain.md)
  The Guided Access error domain.

## Relationships

### Conforms To
- [CustomNSError](../../Foundation/customnserror.md)
- [Equatable](../../Swift/equatable.md)
- [Error](../../Swift/error.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Guided Access
- [static var isGuidedAccessEnabled: Bool](./isguidedaccessenabled.md)
  A Boolean value that indicates whether the Guided Access setting is in an enabled state.
- [static let guidedAccessStatusDidChangeNotification: NSNotification.Name](./guidedaccessstatusdidchangenotification.md)
  A notification that indicates when a Guided Access session starts or ends.
- [static func requestGuidedAccessSession(enabled: Bool, completionHandler: (Bool) -> Void)](./requestguidedaccesssession%28enabled,completionhandler%29.md)
  Transitions the app to or from Single App mode asynchronously.
- [static func configureForGuidedAccess(features: UIGuidedAccessAccessibilityFeature, enabled: Bool, completionHandler: (Bool, (any Error)?) -> Void)](./configureforguidedaccess%28features,enabled,completionhandler%29.md)
  Enables or disables the specified accessibility features while using Guided Access.
- [static func guidedAccessRestrictionState(forIdentifier: String) -> UIAccessibility.GuidedAccessRestrictionState](./guidedaccessrestrictionstate%28foridentifier%29.md)
  Returns the restriction state for the specified guided access restriction.
- [UIAccessibility.GuidedAccessRestrictionState](./guidedaccessrestrictionstate.md)
  Constants that describe the state of a restriction, either allow or deny.
- [static let guidedAccessErrorDomain: String](./guidedaccesserrordomain.md)
  A string that identifies the Guided Access error domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/guidedaccesserror)*