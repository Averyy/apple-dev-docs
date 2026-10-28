# ENDiagnosisReportType.revoked

**Framework**: Exposure Notification  
**Kind**: case  
**Role**: Case

The report is a negative test.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
case revoked
```

```c
ENDiagnosisReportTypeRevoked
```

## Discussion

This case negates a previous self report or clinical diagnosis that may have been in error.

## See Also

### Enumeration Cases
- [ENDiagnosisReportType.confirmedClinicalDiagnosis](./confirmedclinicaldiagnosis.md)
  The report comes from a confirmed clinical diagnosis.
- [ENDiagnosisReportType.confirmedTest](./confirmedtest.md)
  The report comes from a confirmed test.
- [ENDiagnosisReportType.recursive](./recursive.md)
  The report comes from a person determined positive based on exposure to another person confirmed positive.
- [ENDiagnosisReportType.selfReported](./selfreported.md)
  The report comes from the user, without health authority involvement.
- [ENDiagnosisReportType.unknown](./unknown.md)
  The report is an unknown type or is not available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/endiagnosisreporttype/revoked)*