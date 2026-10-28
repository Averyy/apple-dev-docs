# reportTypeRecursiveWeight

**Framework**: Exposure Notification  
**Kind**: property  
**Role**: Instance Property

The weight assigned to a risk level based on an exposure to someone exposed to someone else.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
var reportTypeRecursiveWeight: Double { get set }
```

```objc
@property (nonatomic, assign, readwrite) double reportTypeRecursiveWeight;
```

## Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.7 and later.

This property is unused.

## See Also

### Configuring Report Types
- [var reportTypeConfirmedClinicalDiagnosisWeight: Double](./reporttypeconfirmedclinicaldiagnosisweight.md)
  The weight assigned to a risk level based on a confirmed clinical diagnosis.
- [var reportTypeConfirmedTestWeight: Double](./reporttypeconfirmedtestweight.md)
  The weight assigned to a risk level based on a confirmed test.
- [var reportTypeSelfReportedWeight: Double](./reporttypeselfreportedweight.md)
  The weight assigned to a risk level based on a self-reported diagnoisis.
- [var reportTypeNoneMap: ENDiagnosisReportType](./reporttypenonemap.md)
  The report type to map an unknown diagnosis to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposureconfiguration/reporttyperecursiveweight)*