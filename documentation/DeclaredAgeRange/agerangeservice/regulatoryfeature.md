# AgeRangeService.RegulatoryFeature

**Framework**: Declared Age Range  
**Kind**: enum

Defines the regulatory features that your app may need to support.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+

## Declaration

```swift
enum RegulatoryFeature
```

## Topics

### Checking regulatory requirements
- [AgeRangeService.RegulatoryFeature.declaredAgeRangeRequired](agerangeservice/regulatoryfeature/declaredagerangerequired.md)
  Indicates the person is required to share their age range with your app.
- [AgeRangeService.RegulatoryFeature.significantAppChangeRequiresAdultNotification](agerangeservice/regulatoryfeature/significantappchangerequiresadultnotification.md)
  Indicates that adult users must acknowledge your app’s significant change.
- [AgeRangeService.RegulatoryFeature.significantAppChangeRequiresParentalConsent](agerangeservice/regulatoryfeature/significantappchangerequiresparentalconsent.md)
  Indicates a parent or guardian is required to acknowledge and consent to a significant app change.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var requiredRegulatoryFeatures: Set<AgeRangeService.RegulatoryFeature>](agerangeservice/requiredregulatoryfeatures.md)
  A set of regulatory features that are required for the person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/regulatoryfeature)*