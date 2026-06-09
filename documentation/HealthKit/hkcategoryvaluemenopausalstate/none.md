# HKCategoryValueMenopausalState.none

**Framework**: HealthKit  
**Kind**: case

A value that indicates no menopausal state applies at the sample date.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
case none
```

## Mentions

- [Recording and querying menopausal state](recording-and-querying-menopausal-state.md)

#### Discussion

This value represents a confirmed entry that the person is neither in menopause nor perimenopause at the recorded date. It doesn’t represent unknown, unset, or missing data. Apps can use this value to record that someone explicitly confirmed the absence of a menopausal state at a particular point in time.

## See Also

- [HKCategoryValueMenopausalState.menopause](hkcategoryvaluemenopausalstate/menopause.md)
  A value that indicates the person is in menopause at the sample date.
- [HKCategoryValueMenopausalState.perimenopause](hkcategoryvaluemenopausalstate/perimenopause.md)
  A value that indicates the person is in perimenopause at the sample date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcategoryvaluemenopausalstate/none)*