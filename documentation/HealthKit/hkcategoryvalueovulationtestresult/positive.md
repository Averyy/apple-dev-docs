# positive

**Framework**: HealthKit  
**Kind**: property  
**Role**: Type Property

The ovulation test is positive.

**Availability**:
- iOS 9.0+ - Deprecated in 13.0 (renamed: HKCategoryValueOvulationTestResult.luteinizingHormoneSurge)
- iPadOS 9.0+ - Deprecated in 13.0 (renamed: HKCategoryValueOvulationTestResult.luteinizingHormoneSurge)
- Mac Catalyst 13.1+ - Deprecated in 13.1 (renamed: HKCategoryValueOvulationTestResult.luteinizingHormoneSurge)
- macOS 13.0+
- visionOS 1.0+ - Deprecated in 1.0 (renamed: HKCategoryValueOvulationTestResult.luteinizingHormoneSurge)
- watchOS 2.0+ - Deprecated in 6.0 (renamed: HKCategoryValueOvulationTestResult.luteinizingHormoneSurge)

> **Deprecated**: Use [`HKCategoryValueOvulationTestResult.luteinizingHormoneSurge`](./luteinizinghormonesurge.md) instead.

## Declaration

```swift
static var positive: HKCategoryValueOvulationTestResult { get }
```

```c
HKCategoryValueOvulationTestResultPositive
```

## See Also

### Ovulation Test Results
- [HKCategoryValueOvulationTestResult.negative](./negative.md)
  The ovulation test is negative.
- [HKCategoryValueOvulationTestResult.luteinizingHormoneSurge](./luteinizinghormonesurge.md)
  The ovulation test detected a surge in the luteinizing hormone. This value often refers to a `Positive` or `Peak` result.
- [HKCategoryValueOvulationTestResult.indeterminate](./indeterminate.md)
  The ovulation test is inconclusive.
- [HKCategoryValueOvulationTestResult.estrogenSurge](./estrogensurge.md)
  The ovulation test detected a surge in estrogen. This value often refers to a `High` result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcategoryvalueovulationtestresult/positive)*