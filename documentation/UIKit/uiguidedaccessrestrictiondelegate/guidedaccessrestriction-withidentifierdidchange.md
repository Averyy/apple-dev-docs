# guidedAccessRestriction(withIdentifier:didChange:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Tells the delegate that the restriction associated with the identifier has changed state.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func guidedAccessRestriction(withIdentifier restrictionIdentifier: String, didChange newRestrictionState: UIAccessibility.GuidedAccessRestrictionState)
```

#### Discussion

Your app should adjust its behavior to allow or deny the operation controlled by the specified restriction each time it receives this message.

## Parameters

- `restrictionIdentifier`: The identifier of the restriction whose state has changed.
- `newRestrictionState`: The new state for the restriction.

## See Also

- [UIAccessibility.GuidedAccessRestrictionState](uiaccessibility/guidedaccessrestrictionstate.md)
  Constants that describe the state of a restriction, either allow or deny.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiguidedaccessrestrictiondelegate/guidedaccessrestriction(withidentifier:didchange:))*