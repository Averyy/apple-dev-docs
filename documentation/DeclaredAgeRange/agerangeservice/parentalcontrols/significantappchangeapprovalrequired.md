# significantAppChangeApprovalRequired

**Framework**: Declared Age Range  
**Kind**: property  
**Role**: Type Property

Indicates a notification obligation for significant app updates.

**Availability**:
- iOS 26.2+ - Deprecated in 26.4
- iPadOS 26.2+ - Deprecated in 26.4
- Mac Catalyst 26.2+ - Deprecated in 26.4
- macOS 26.2+ - Deprecated in 26.4

> **Deprecated**: Use requiredRegulatoryFeatures to check for significantAppChangeRequiresParentalConsent instead

## Declaration

```swift
static let significantAppChangeApprovalRequired: AgeRangeService.ParentalControls
```

## Mentions

- [Requesting people’s age range information in your app](../../requesting-people-share-their-age-range-with-your-app.md)

#### Discussion

When this option is present, notify the parent or guardian before implementing significant app changes or updates to comply with associated laws or regulations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/parentalcontrols/significantappchangeapprovalrequired)*