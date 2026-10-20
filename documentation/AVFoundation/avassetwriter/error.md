# error

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An error object that describes an asset-writing failure.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var error: (any Error)? { get }
```

```objc
@property (readonly, nullable) NSError * error;
```

## See Also

### Inspecting writing status
- [var status: AVAssetWriter.Status](./status-swift.property.md)
  The status of writing samples to the output file.
- [AVAssetWriter.Status](./status-swift.enum.md)
  Values that indicate the state of an asset writer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/error)*