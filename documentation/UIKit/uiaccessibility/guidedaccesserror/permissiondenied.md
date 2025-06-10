# permissionDenied

**Framework**: UIKit  
**Kind**: property

An error that indicates the app isn’t authorized to perform the requested action.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
static var permissionDenied: UIAccessibility.GuidedAccessError.Code { get }
```

#### Discussion

For example, this error might indicate that your app is requesting a configuration change but isn’t locked into Single App Mode through a configuration profile.

## See Also

- [static var failed: UIAccessibility.GuidedAccessError.Code](uiaccessibility/guidedaccesserror/failed.md)
  An error that indicates a failure for an unspecified reason.
- [UIAccessibility.GuidedAccessError.Code](uiaccessibility/guidedaccesserror/code.md)
  Error codes for Guided Access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/guidedaccesserror/permissiondenied)*