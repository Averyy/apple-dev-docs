# status

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The status of writing samples to the output file.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var status: AVAssetWriter.Status { get }
```

```objc
@property (readonly) AVAssetWriterStatus status;
```

## Discussion

This property is thread safe.

## See Also

### Inspecting writing status
- [AVAssetWriter.Status](./status-swift.enum.md)
  Values that indicate the state of an asset writer.
- [var error: (any Error)?](./error.md)
  An error object that describes an asset-writing failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/status-swift.property)*