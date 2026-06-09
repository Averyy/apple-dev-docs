# menopausalState

**Framework**: HealthKit  
**Kind**: property

An identifier for samples that record a person’s menopausal state.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
static let menopausalState: HKCategoryTypeIdentifier
```

## Mentions

- [Recording and querying menopausal state](recording-and-querying-menopausal-state.md)

#### Discussion

Use this category type to record which menopausal state applies at a specific point in time. Each sample is a point-in-time entry where the start date equals the end date, and the value is one of the [`HKCategoryValueMenopausalState`](hkcategoryvaluemenopausalstate.md) cases: [`HKCategoryValueMenopausalState.menopause`](hkcategoryvaluemenopausalstate/menopause.md), [`HKCategoryValueMenopausalState.perimenopause`](hkcategoryvaluemenopausalstate/perimenopause.md), or [`HKCategoryValueMenopausalState.none`](hkcategoryvaluemenopausalstate/none.md).

Apps can interpret these point-in-time samples as state changes, confirmations that a state applied at a particular date, or both. When creating a menopausal state sample, the framework requires that the start date and end date be identical. Attempting to save a sample where these dates differ results in an error.

## See Also

- [Recording and querying menopausal state](recording-and-querying-menopausal-state.md)
  Personalize someone’s experience on a health app by tracking the information they record on menopausal state.
- [static let bleedingAfterMenopause: HKCategoryTypeIdentifier](hkcategorytypeidentifier/bleedingaftermenopause.md)
  An identifier for samples that record bleeding after menopause.
- [enum HKCategoryValueMenopausalState](hkcategoryvaluemenopausalstate.md)
  A value that indicates the menopausal state at a recorded point in time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier/menopausalstate)*