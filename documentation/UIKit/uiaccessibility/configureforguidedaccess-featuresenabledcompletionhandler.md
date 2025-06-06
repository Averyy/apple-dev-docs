# configureForGuidedAccess(features:enabled:completionHandler:)

**Framework**: UIKit  
**Kind**: method

Enables or disables the specified accessibility features while using Guided Access.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
static func configureForGuidedAccess(features: UIGuidedAccessAccessibilityFeature, enabled: Bool, completionHandler completion: @escaping (Bool, (any Error)?) -> Void)
```

## See Also

- [struct UIGuidedAccessAccessibilityFeature](uiguidedaccessaccessibilityfeature.md)
  Constants that describe accessibility features for Guided Access.
- [UIAccessibility.GuidedAccessError.Code](uiaccessibility/guidedaccesserror/code.md)
  Error codes for Guided Access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/configureforguidedaccess(features:enabled:completionhandler:))*