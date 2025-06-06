# textForGuidedAccessRestriction(withIdentifier:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Provides a succinct description of the restriction for the specified identifier.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func textForGuidedAccessRestriction(withIdentifier restrictionIdentifier: String) -> String?
```

#### Return Value

A localized, human-readable string that succinctly describes the restriction for the provided identifier.

## Parameters

- `restrictionIdentifier`: The identifer of the restriction the system is interested in.

## See Also

- [var guidedAccessRestrictionIdentifiers: [String]?](uiguidedaccessrestrictiondelegate/guidedaccessrestrictionidentifiers.md)
  An array of strings identifying custom restrictions.
- [func detailTextForGuidedAccessRestriction(withIdentifier: String) -> String?](uiguidedaccessrestrictiondelegate/detailtextforguidedaccessrestriction(withidentifier:).md)
  Provides more detailed information about the restriction for the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiguidedaccessrestrictiondelegate/textforguidedaccessrestriction(withidentifier:))*