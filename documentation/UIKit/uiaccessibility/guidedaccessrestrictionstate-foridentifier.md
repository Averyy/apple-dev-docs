# guidedAccessRestrictionState(forIdentifier:)

**Framework**: UIKit  
**Kind**: method

Returns the restriction state for the specified guided access restriction.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
static func guidedAccessRestrictionState(forIdentifier restrictionIdentifier: String) -> UIAccessibility.GuidedAccessRestrictionState
```

#### Return Value

The current state of the guided access restriction. The initial state of all restrictions is [`UIAccessibility.GuidedAccessRestrictionState.allow`](uiaccessibility/guidedaccessrestrictionstate/allow.md).

## Parameters

- `restrictionIdentifier`: The string that uniquely identifies the guided access restriction.

## See Also

- [protocol UIGuidedAccessRestrictionDelegate](uiguidedaccessrestrictiondelegate.md)
  A set of methods you use to add custom restrictions for the Guided Access feature in iOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/guidedaccessrestrictionstate(foridentifier:))*