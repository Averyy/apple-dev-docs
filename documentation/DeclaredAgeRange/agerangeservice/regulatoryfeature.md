# AgeRangeService.RegulatoryFeature

**Framework**: Declared Age Range  
**Kind**: enum  
**Role**: Enumeration

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
- [AgeRangeService.RegulatoryFeature.declaredAgeRangeRequired](./regulatoryfeature/declaredagerangerequired.md)
  Indicates the person is required to share their age range with your app.
- [AgeRangeService.RegulatoryFeature.significantAppChangeRequiresAdultNotification](./regulatoryfeature/significantappchangerequiresadultnotification.md)
  Indicates that adult users must acknowledge your app’s significant change.
- [AgeRangeService.RegulatoryFeature.significantAppChangeRequiresParentalConsent](./regulatoryfeature/significantappchangerequiresparentalconsent.md)
  Indicates a parent or guardian is required to acknowledge and consent to a significant app change.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Defining regulatory features
- [var requiredRegulatoryFeatures: Set<AgeRangeService.RegulatoryFeature>](./requiredregulatoryfeatures.md)
  A set of regulatory features that are required for the person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/regulatoryfeature)*