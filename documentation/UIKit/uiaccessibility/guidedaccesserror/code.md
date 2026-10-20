# UIAccessibility.GuidedAccessError.Code

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum UIGuidedAccessErrorCode : NSInteger;
```

## Topics

### Errors
- [UIAccessibility.GuidedAccessError.Code.permissionDenied](./code/permissiondenied.md)
  An error that indicates the app isn’t authorized to perform the requested action.
- [UIAccessibility.GuidedAccessError.Code.failed](./code/failed.md)
  An error that indicates a failure for an unspecified reason.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../../Swift/bitwisecopyable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Guided Access
- [static func configureForGuidedAccess(features: UIGuidedAccessAccessibilityFeature, enabled: Bool, completionHandler: (Bool, (any Error)?) -> Void)](../configureforguidedaccess%28features,enabled,completionhandler%29.md)
  Enables or disables the specified accessibility features while using Guided Access.
- [struct UIGuidedAccessAccessibilityFeature](../../uiguidedaccessaccessibilityfeature.md)
  Constants that describe accessibility features for Guided Access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/guidedaccesserror/code)*