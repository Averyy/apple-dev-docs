# ENDiagnosisReportType.revoked

**Framework**: Exposure Notification  
**Kind**: case

The report is a negative test.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
case revoked
```

#### Discussion

This case negates a previous self report or clinical diagnosis that may have been in error.

## See Also

- [ENDiagnosisReportType.confirmedClinicalDiagnosis](endiagnosisreporttype/confirmedclinicaldiagnosis.md)
  The report comes from a confirmed clinical diagnosis.
- [ENDiagnosisReportType.confirmedTest](endiagnosisreporttype/confirmedtest.md)
  The report comes from a confirmed test.
- [ENDiagnosisReportType.recursive](endiagnosisreporttype/recursive.md)
  The report comes from a person determined positive based on exposure to another person confirmed positive.
- [ENDiagnosisReportType.selfReported](endiagnosisreporttype/selfreported.md)
  The report comes from the user, without health authority involvement.
- [ENDiagnosisReportType.unknown](endiagnosisreporttype/unknown.md)
  The report is an unknown type or is not available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/endiagnosisreporttype/revoked)*