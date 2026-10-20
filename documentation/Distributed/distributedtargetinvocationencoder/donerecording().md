# doneRecording()

**Framework**: Distributed  
**Kind**: method  
**Required**: Yes

Invoked to signal to the encoder that no further `record...` calls will be made on it.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
mutating func doneRecording() throws
```

#### Discussion

Useful if the encoder needs to perform some “final” task before the underlying message is considered complete, e.g. computing a checksum, or some additional message signing or finalization step.


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/distributedtargetinvocationencoder/donerecording())*