# UIAccessibility.GuidedAccessError

**Framework**: UIKit  
**Kind**: struct

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
- [static var permissionDenied: UIAccessibility.GuidedAccessError.Code](uiaccessibility/guidedaccesserror/permissiondenied.md)
  An error that indicates the app isn’t authorized to perform the requested action.
- [static var failed: UIAccessibility.GuidedAccessError.Code](uiaccessibility/guidedaccesserror/failed.md)
  An error that indicates a failure for an unspecified reason.
- [UIAccessibility.GuidedAccessError.Code](uiaccessibility/guidedaccesserror/code.md)
  Error codes for Guided Access.
### Getting error information
- [static var errorDomain: String](uiaccessibility/guidedaccesserror/errordomain.md)
  The Guided Access error domain.

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [static var isGuidedAccessEnabled: Bool](uiaccessibility/isguidedaccessenabled.md)
  A Boolean value that indicates whether the Guided Access setting is in an enabled state.
- [static let guidedAccessStatusDidChangeNotification: NSNotification.Name](uiaccessibility/guidedaccessstatusdidchangenotification.md)
  A notification that indicates when a Guided Access session starts or ends.
- [static func requestGuidedAccessSession(enabled: Bool, completionHandler: (Bool) -> Void)](uiaccessibility/requestguidedaccesssession(enabled:completionhandler:).md)
  Transitions the app to or from Single App mode asynchronously.
- [static func configureForGuidedAccess(features: UIGuidedAccessAccessibilityFeature, enabled: Bool, completionHandler: (Bool, (any Error)?) -> Void)](uiaccessibility/configureforguidedaccess(features:enabled:completionhandler:).md)
  Enables or disables the specified accessibility features while using Guided Access.
- [static func guidedAccessRestrictionState(forIdentifier: String) -> UIAccessibility.GuidedAccessRestrictionState](uiaccessibility/guidedaccessrestrictionstate(foridentifier:).md)
  Returns the restriction state for the specified guided access restriction.
- [UIAccessibility.GuidedAccessRestrictionState](uiaccessibility/guidedaccessrestrictionstate.md)
  Constants that describe the state of a restriction, either allow or deny.
- [static let guidedAccessErrorDomain: String](uiaccessibility/guidedaccesserrordomain.md)
  A string that identifies the Guided Access error domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/guidedaccesserror)*