# guidedAccessErrorDomain

**Framework**: UIKit  
**Kind**: property

A string that identifies the Guided Access error domain.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 13.1+
- tvOS 12.2+
- visionOS 1.0+

## Declaration

```swift
nonisolated
static let guidedAccessErrorDomain: String
```

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
- [UIAccessibility.GuidedAccessError](uiaccessibility/guidedaccesserror.md)
  A Guided Access error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/guidedaccesserrordomain)*