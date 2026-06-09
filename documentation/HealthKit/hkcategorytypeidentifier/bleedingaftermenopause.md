# bleedingAfterMenopause

**Framework**: HealthKit  
**Kind**: property

An identifier for samples that record bleeding after menopause.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
static let bleedingAfterMenopause: HKCategoryTypeIdentifier
```

#### Discussion

Use this category type to record instances of bleeding that occur after menopause. After menopause, menstruation has ended, making this clinically distinct from menstrual flow or intermenstrual bleeding. Each sample represents an interval of bleeding and stores an intensity value using [`HKCategoryValueVaginalBleeding`](hkcategoryvaluevaginalbleeding.md).

For information about menopause state tracking, see [`menopausalState`](hkcategorytypeidentifier/menopausalstate.md).

## See Also

- [Recording and querying menopausal state](recording-and-querying-menopausal-state.md)
  Personalize someone’s experience on a health app by tracking the information they record on menopausal state.
- [static let menopausalState: HKCategoryTypeIdentifier](hkcategorytypeidentifier/menopausalstate.md)
  An identifier for samples that record a person’s menopausal state.
- [enum HKCategoryValueMenopausalState](hkcategoryvaluemenopausalstate.md)
  A value that indicates the menopausal state at a recorded point in time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier/bleedingaftermenopause)*