# finishSeries(metadata:endDate:completion:)

**Framework**: Healthkit  
**Kind**: method

Finalizes the series with the provided end date, and returns the resulting quantity samples.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func finishSeries(metadata: [String : Any]?, endDate: Date?) async throws -> [HKQuantitySample]
```

#### Discussion

Call [`finishSeries(metadata:endDate:completion:)`](hkquantityseriessamplebuilder/finishseries(metadata:enddate:completion:).md) after inserting all the quantities for the series. The series builder then creates one or more samples to represent the series, saves the samples to the HealthKit store, and then passes them to the completion handler.

> **Note**:  The series builder typically creates a single sample that contains all the inserted quantities; however, it may split the quantities up into multiple sample objects.

Calling this method before inserting any samples results in an error. Also, calling this method invalidates the series builder; you cannot call any other series builder methods after calling this method.

## Parameters

- `metadata`: Using predefined keys helps facilitate sharing data between apps; however, you are also encouraged to create your own, custom keys as needed to extend the samples’ capabilities.
- `endDate`: The sample builder returns an   error if the   is earlier than the builder’s   parameter, or is earlier than the end date of any of the quantities inserted into the builder.
- `completion`: The handler takes the following parameters:

## See Also

- [func discard()](hkquantityseriessamplebuilder/discard.md)
  Discards all previously collected data and invalidates the builder.
- [func finishSeries(metadata: [String : Any]?, completion: ([HKQuantitySample]?, (any Error)?) -> Void)](hkquantityseriessamplebuilder/finishseries(metadata:completion:).md)
  Finalizes the series and returns the resulting quantity samples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantityseriessamplebuilder/finishseries(metadata:enddate:completion:))*