# dataOutputSynchronizer(_:didOutput:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Provides a collection of synchronized capture data to the delegate.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
func dataOutputSynchronizer(_ synchronizer: AVCaptureDataOutputSynchronizer, didOutput synchronizedDataCollection: AVCaptureSynchronizedDataCollection)
```

```objc
- (void) dataOutputSynchronizer:(AVCaptureDataOutputSynchronizer *) synchronizer didOutputSynchronizedDataCollection:(AVCaptureSynchronizedDataCollection *) synchronizedDataCollection;
```

## Discussion

Use the data collection’s [`synchronizedData(for:)`](../avcapturesynchronizeddatacollection/synchronizeddata%28for%29.md) method (or equivalent [`subscript(_:)`](../avcapturesynchronizeddatacollection/subscript%28_%29.md) operator) to retrieve the captured data corresponding to each capture output.

## Parameters

- `synchronizer`: The synchronizer object delivering synchronized data.
- `synchronizedDataCollection`: A collection of data samples, one for each capture output governed by the data output synchronizer for which capture data is ready.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedataoutputsynchronizerdelegate/dataoutputsynchronizer(_:didoutput:))*