# requestReadData(atOffset:length:completion:)

**Framework**: ImageCaptureCore  
**Kind**: method

Requests to asynchronously read data of a specified length from a specified offset, then executes the completion block.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func requestReadData(atOffset offset: off_t, length: off_t) async throws -> Data
```

#### Discussion

The completion block executes on an any available queue; often this is not the main queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccamerafile/requestreaddata(atoffset:length:completion:))*