# infectiousnessHighWeight

**Framework**: Exposure Notification  
**Kind**: property  
**Role**: Instance Property

The weight to apply for severe infectiousness.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
var infectiousnessHighWeight: Double { get set }
```

```objc
@property (nonatomic, assign, readwrite) double infectiousnessHighWeight;
```

#### Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.7 and later.

The range of this value is 0-250%.

## See Also

### Configuring Infectiousness
- [var infectiousnessForDaysSinceOnsetOfSymptoms: [NSNumber : NSNumber]?](./infectiousnessfordayssinceonsetofsymptoms.md)
  The mapping between the days since onset of symptoms to the degree of infectiousness.
- [var infectiousnessStandardWeight: Double](./infectiousnessstandardweight.md)
  The weight to apply for mild infectiousness.
- [var ENDaysSinceOnsetOfSymptomsUnknown: Int](../endayssinceonsetofsymptomsunknown.md)
  A value used when the number of days since onset of symptoms is unknown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposureconfiguration/infectiousnesshighweight)*