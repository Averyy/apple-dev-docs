# ENDaysSinceOnsetOfSymptomsUnknown

**Framework**: Exposure Notification  
**Kind**: var  
**Role**: Global Variable

A value used when the number of days since onset of symptoms is unknown.

**Availability**:
- iOS 14.0+ - Deprecated in 14.2
- iPadOS 14.0+ - Deprecated in 14.2
- Mac Catalyst 14.0+ - Deprecated in 14.2

> **Deprecated**: Server must provide keys with days_since_onset_of_symptoms set.

## Declaration

```swift
var ENDaysSinceOnsetOfSymptomsUnknown: Int { get }
```

```c
static const NSInteger ENDaysSinceOnsetOfSymptomsUnknown;
```

#### Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 14.0 and later.

## See Also

### Configuring Infectiousness
- [var infectiousnessForDaysSinceOnsetOfSymptoms: [NSNumber : NSNumber]?](./enexposureconfiguration/infectiousnessfordayssinceonsetofsymptoms.md)
  The mapping between the days since onset of symptoms to the degree of infectiousness.
- [var infectiousnessHighWeight: Double](./enexposureconfiguration/infectiousnesshighweight.md)
  The weight to apply for severe infectiousness.
- [var infectiousnessStandardWeight: Double](./enexposureconfiguration/infectiousnessstandardweight.md)
  The weight to apply for mild infectiousness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/endayssinceonsetofsymptomsunknown)*