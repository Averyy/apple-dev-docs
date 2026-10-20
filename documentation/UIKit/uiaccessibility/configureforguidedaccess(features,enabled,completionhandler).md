# configureForGuidedAccess(features:enabled:completionHandler:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

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

```c
extern void UIGuidedAccessConfigureAccessibilityFeatures(UIGuidedAccessAccessibilityFeature features, BOOL enabled, void (^completion)(BOOL success, NSError *error));
```

## See Also

### Guided Access
- [struct UIGuidedAccessAccessibilityFeature](../uiguidedaccessaccessibilityfeature.md)
  Constants that describe accessibility features for Guided Access.
- [UIAccessibility.GuidedAccessError.Code](./guidedaccesserror/code.md)
  Error codes for Guided Access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/configureforguidedaccess(features:enabled:completionhandler:))*