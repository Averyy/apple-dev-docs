# UIAccessibility.GuidedAccessRestrictionState

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the state of a restriction, either allow or deny.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum GuidedAccessRestrictionState
```

```c
enum UIGuidedAccessRestrictionState : NSInteger;
```

## Topics

### Constants
- [UIAccessibility.GuidedAccessRestrictionState.allow](./guidedaccessrestrictionstate/allow.md)
  The app should allow the user to perform the action controlled by the restriction.
- [UIAccessibility.GuidedAccessRestrictionState.deny](./guidedaccessrestrictionstate/deny.md)
  The app should deny the user from performing the action controlled by the restriction.
### Initializers
- [init?(rawValue: Int)](./guidedaccessrestrictionstate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Implementing restrictions
- [func guidedAccessRestriction(withIdentifier: String, didChange: UIAccessibility.GuidedAccessRestrictionState)](../uiguidedaccessrestrictiondelegate/guidedaccessrestriction%28withidentifier,didchange%29.md)
  Tells the delegate that the restriction associated with the identifier has changed state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/guidedaccessrestrictionstate)*