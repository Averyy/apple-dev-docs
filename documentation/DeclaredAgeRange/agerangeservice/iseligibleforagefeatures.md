# isEligibleForAgeFeatures

**Framework**: Declared Age Range  
**Kind**: property

A boolean value that indicates whether an adult, teen, or child is eligible for age gated features.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
var isEligibleForAgeFeatures: Bool { get async throws }
```

#### Return Value

`true` if your app is eligible for age gated features; otherwise, `false`.

#### Discussion

Use this property to determine whether a person using your app is in an applicable region that requires additional age-related obligations for when you distribute apps on the App Store. For more information, refer to [`Next steps for apps distributed in Texas`](https://developer.apple.comhttps://developer.apple.com/news/?id=2ezb6jhj).

This flag returns `true` on iOS and iPadOS based on a person’s eligibility and always returns `false` on macOS.

> **Note**: [`AgeRangeService.Error.notAvailable`](agerangeservice/error/notavailable.md) if the age gate service is unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/iseligibleforagefeatures)*