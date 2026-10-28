# infectiousnessForDaysSinceOnsetOfSymptoms

**Framework**: Exposure Notification  
**Kind**: property  
**Role**: Instance Property

The mapping between the days since onset of symptoms to the degree of infectiousness.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
var infectiousnessForDaysSinceOnsetOfSymptoms: [NSNumber : NSNumber]? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) NSDictionary<NSNumber *,NSNumber *> * infectiousnessForDaysSinceOnsetOfSymptoms;
```

## Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.7 and later.

The dictionary key is the day since the onset of symptoms. The corresponding value is an [`ENInfectiousness`](../eninfectiousness.md) value. When the day is not known, use [`ENDaysSinceOnsetOfSymptomsUnknown`](../endayssinceonsetofsymptomsunknown.md) as the dictionary key, like this:

```swift
infectiousnessForDaysSinceOnsetOfSymptoms[ENDaysSinceOnsetOfSymptionsUnknown] = 
        infectiousnessHighWeight;
```

You can’t change this property more often than once per week. During development, you can remove this limitation by adding the test entitlement `com.apple.developer.exposure-notification-test` to your project.

> **Note**:  You must set this property when using the version 2 scoring algorithm.

## See Also

### Configuring Infectiousness
- [var infectiousnessHighWeight: Double](./infectiousnesshighweight.md)
  The weight to apply for severe infectiousness.
- [var infectiousnessStandardWeight: Double](./infectiousnessstandardweight.md)
  The weight to apply for mild infectiousness.
- [var ENDaysSinceOnsetOfSymptomsUnknown: Int](../endayssinceonsetofsymptomsunknown.md)
  A value used when the number of days since onset of symptoms is unknown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposureconfiguration/infectiousnessfordayssinceonsetofsymptoms)*