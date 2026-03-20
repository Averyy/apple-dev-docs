# requiredRegulatoryFeatures

**Framework**: Declared Age Range  
**Kind**: property

A set of regulatory features that are required for the person.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+

## Declaration

```swift
var requiredRegulatoryFeatures: Set<AgeRangeService.RegulatoryFeature> { get async throws }
```

#### Return Value

A set of [`AgeRangeService.RegulatoryFeature`](agerangeservice/regulatoryfeature.md) values indicating which regulatory requirements apply to the person.

#### Discussion

Use this property to determine which regulatory features apply to a person using your app based on their region and account settings. This helps you comply with regional requirements when distributing apps on the App Store. For more information, refer to [`Next steps for apps distributed in Texas`](https://developer.apple.comhttps://developer.apple.com/news/?id=2ezb6jhj).

> **Note**:  [`AgeRangeService.Error.notAvailable`](agerangeservice/error/notavailable.md) if the regulatory feature’s service is unavailable.

## See Also

- [AgeRangeService.RegulatoryFeature](agerangeservice/regulatoryfeature.md)
  Defines the regulatory features that your app may need to support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/requiredregulatoryfeatures)*