# guidedAccessRestrictionIdentifiers

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

An array of strings identifying custom restrictions.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var guidedAccessRestrictionIdentifiers: [String]? { get }
```

#### Return Value

An array of NSString objects, each of which represents a custom restriction.

#### Discussion

Your delegate must implement this method and return an array with an identifier string for each custom guided access restriction you wish to provide in your app.

## See Also

- [func textForGuidedAccessRestriction(withIdentifier: String) -> String?](uiguidedaccessrestrictiondelegate/textforguidedaccessrestriction(withidentifier:).md)
  Provides a succinct description of the restriction for the specified identifier.
- [func detailTextForGuidedAccessRestriction(withIdentifier: String) -> String?](uiguidedaccessrestrictiondelegate/detailtextforguidedaccessrestriction(withidentifier:).md)
  Provides more detailed information about the restriction for the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiguidedaccessrestrictiondelegate/guidedaccessrestrictionidentifiers)*