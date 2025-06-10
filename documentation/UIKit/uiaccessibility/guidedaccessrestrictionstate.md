# UIAccessibility.GuidedAccessRestrictionState

**Framework**: UIKit  
**Kind**: enum

Constants that describe the state of a restriction, either allow or deny.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum GuidedAccessRestrictionState
```

## Topics

### Constants
- [UIAccessibility.GuidedAccessRestrictionState.allow](uiaccessibility/guidedaccessrestrictionstate/allow.md)
  The app should allow the user to perform the action controlled by the restriction.
- [UIAccessibility.GuidedAccessRestrictionState.deny](uiaccessibility/guidedaccessrestrictionstate/deny.md)
  The app should deny the user from performing the action controlled by the restriction.
### Initializers
- [init?(rawValue: Int)](uiaccessibility/guidedaccessrestrictionstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func guidedAccessRestriction(withIdentifier: String, didChange: UIAccessibility.GuidedAccessRestrictionState)](uiguidedaccessrestrictiondelegate/guidedaccessrestriction(withidentifier:didchange:).md)
  Tells the delegate that the restriction associated with the identifier has changed state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/guidedaccessrestrictionstate)*