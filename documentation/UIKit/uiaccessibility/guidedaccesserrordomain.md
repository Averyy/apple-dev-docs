# guidedAccessErrorDomain

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

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

```c
extern NSErrorDomain const UIGuidedAccessErrorDomain;
```

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
- [UIAccessibility.GuidedAccessError](./guidedaccesserror.md)
  A Guided Access error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/guidedaccesserrordomain)*