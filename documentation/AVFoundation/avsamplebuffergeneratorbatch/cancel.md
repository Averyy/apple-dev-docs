# cancel()

**Framework**: AVFoundation  
**Kind**: method

Cancels any I/O for this batch.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func cancel()
```

#### Discussion

The system invokes the associated sample buffers data ready handlers with an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffergeneratorbatch/cancel())*