# detailTextForGuidedAccessRestriction(withIdentifier:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Provides more detailed information about the restriction for the specified identifier.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func detailTextForGuidedAccessRestriction(withIdentifier restrictionIdentifier: String) -> String?
```

```objc
- (NSString *) detailTextForGuidedAccessRestrictionWithIdentifier:(NSString *) restrictionIdentifier;
```

## Return Value

A localized, human-readable string that provides additional information about the restriction for the provided identifier.

## Parameters

- `restrictionIdentifier`: The identifer of the restriction the system is interested in.

## See Also

### Identifying custom Guided Access restrictions
- [var guidedAccessRestrictionIdentifiers: [String]?](./guidedaccessrestrictionidentifiers.md)
  An array of strings identifying custom restrictions.
- [func textForGuidedAccessRestriction(withIdentifier: String) -> String?](./textforguidedaccessrestriction%28withidentifier%29.md)
  Provides a succinct description of the restriction for the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiguidedaccessrestrictiondelegate/detailtextforguidedaccessrestriction(withidentifier:))*