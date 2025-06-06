# addMetadata(_:completion:)

**Framework**: HealthKit  
**Kind**: method

Adds metadata to the sample.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func addMetadata(_ metadata: [String : Any]) async throws
```

#### Discussion

The builder adds the metadata to the resulting series sample. It incorporates new data using [`addEntries(from:)`](https://developer.apple.com/documentation/foundation/nsmutabledictionary/1411035-addentries).

## Parameters

- `metadata`: Using predefined keys helps facilitate sharing data between apps; however, you are also encouraged to create your own, custom keys as needed to extend the samples’ capabilities.
- `completion`: The completion handler called by the builder after it attempts to add the metadata to the series. The completion handler takes the following parameters:

## See Also

- [func addHeartbeatWithTimeInterval(sinceSeriesStartDate: TimeInterval, precededByGap: Bool, completion: (Bool, (any Error)?) -> Void)](hkheartbeatseriesbuilder/addheartbeatwithtimeinterval(sinceseriesstartdate:precededbygap:completion:).md)
  Adds a heartbeat to the series.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkheartbeatseriesbuilder/addmetadata(_:completion:))*