# isEligibleForAgeFeatures

**Framework**: Declared Age Range  
**Kind**: property

A Boolean value that indicates whether an adult, teen, or child is eligible for age-gated features.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- macOS 26.2+

## Declaration

```swift
var isEligibleForAgeFeatures: Bool { get async throws }
```

#### Return Value

`true` if your app is eligible for age-gated features; otherwise, `false`.

#### Discussion

Before implementing age-gated features in your app, check whether the person using your app is in a region that requires Age Assurance. For more information, refer to [`Next steps for apps distributed in Texas`](https://developer.apple.comhttps://developer.apple.com/news/?id=2ezb6jhj). Use [`isEligibleForAgeFeatures`](agerangeservice/iseligibleforagefeatures.md) to determine whether associated laws or regulations may apply to your app based on the person’s location and account settings. This property returns `true` when your app needs to support Age Assurance for the current user. In macOS, [`isEligibleForAgeFeatures`](agerangeservice/iseligibleforagefeatures.md) returns `false` because the system doesn’t require Age Assurance for the person or device. However, you can still call `requestAgeRange` in macOS to get the declared age range.

> **Note**: [`AgeRangeService.Error.notAvailable`](agerangeservice/error/notavailable.md) if it’s unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/iseligibleforagefeatures)*