# detailTextForGuidedAccessRestriction(withIdentifier:)

**Framework**: UIKit  
**Kind**: method

Provides more detailed information about the restriction for the specified identifier.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func detailTextForGuidedAccessRestriction(withIdentifier restrictionIdentifier: String) -> String?
```

#### Return Value

A localized, human-readable string that provides additional information about the restriction for the provided identifier.

## Parameters

- `restrictionIdentifier`: The identifer of the restriction the system is interested in.

## See Also

- [var guidedAccessRestrictionIdentifiers: [String]?](uiguidedaccessrestrictiondelegate/guidedaccessrestrictionidentifiers.md)
  An array of strings identifying custom restrictions.
- [func textForGuidedAccessRestriction(withIdentifier: String) -> String?](uiguidedaccessrestrictiondelegate/textforguidedaccessrestriction(withidentifier:).md)
  Provides a succinct description of the restriction for the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiguidedaccessrestrictiondelegate/detailtextforguidedaccessrestriction(withidentifier:))*