# finishSeries(completion:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Finalizes the series and returns the resulting heartbeat series sample.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func finishSeries(completion: @escaping @Sendable (HKHeartbeatSeriesSample?, (any Error)?) -> Void)
```

```swift
func finishSeries() async throws -> HKHeartbeatSeriesSample
```

```objc
- (void) finishSeriesWithCompletion:(void (^)(HKHeartbeatSeriesSample *heartbeatSeries, NSError *error)) completion;
```

## Discussion

Call [`finishSeries(completion:)`](./finishseries%28completion%29.md) after inserting all the heartbeats for the series. The series builder creates the series sample, saves it to the HealthKit store, and passes it to the completion handler.

Calling this method before inserting any heartbeats results in an error. Also, calling this method invalidates the series builder; you cannot call any other series builder methods after calling this method.

## Parameters

- `completion`: The completion handler called by the builder after it attempts to create and save the heartbeat series sample. The completion handler takes the following parameters:

  - **`heartbeatSeries`**: If successful it contains the resuting sample; otherwise, `nil`.
  - **`error`**: If an error occurs, this contains an object that describes the error; otherwise, `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkheartbeatseriesbuilder/finishseries(completion:))*