# UIAccessibility.GuidedAccessError.Code

**Framework**: UIKit  
**Kind**: enum

Error codes for Guided Access.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

## Topics

### Errors
- [UIAccessibility.GuidedAccessError.Code.permissionDenied](uiaccessibility/guidedaccesserror/code/permissiondenied.md)
  An error that indicates the app isn’t authorized to perform the requested action.
- [UIAccessibility.GuidedAccessError.Code.failed](uiaccessibility/guidedaccesserror/code/failed.md)
  An error that indicates a failure for an unspecified reason.
### Initializers
- [init?(rawValue: Int)](uiaccessibility/guidedaccesserror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static func configureForGuidedAccess(features: UIGuidedAccessAccessibilityFeature, enabled: Bool, completionHandler: (Bool, (any Error)?) -> Void)](uiaccessibility/configureforguidedaccess(features:enabled:completionhandler:).md)
  Enables or disables the specified accessibility features while using Guided Access.
- [struct UIGuidedAccessAccessibilityFeature](uiguidedaccessaccessibilityfeature.md)
  Constants that describe accessibility features for Guided Access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/guidedaccesserror/code)*