# infectiousnessHighWeight

**Framework**: Exposure Notification  
**Kind**: property

The weight to apply for severe infectiousness.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
var infectiousnessHighWeight: Double { get set }
```

#### Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.7 and later.

The range of this value is 0-250%.

## See Also

- [var infectiousnessForDaysSinceOnsetOfSymptoms: [NSNumber : NSNumber]?](enexposureconfiguration/infectiousnessfordayssinceonsetofsymptoms.md)
  The mapping between the days since onset of symptoms to the degree of infectiousness.
- [var infectiousnessStandardWeight: Double](enexposureconfiguration/infectiousnessstandardweight.md)
  The weight to apply for mild infectiousness.
- [let ENDaysSinceOnsetOfSymptomsUnknown: Int](endayssinceonsetofsymptomsunknown.md)
  A value used when the number of days since onset of symptoms is unknown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposureconfiguration/infectiousnesshighweight)*