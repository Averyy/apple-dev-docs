# init(windowDuration:overlapFactor:)

**Framework**: Create ML Components  
**Kind**: init

Creates an audio feature print feature extractor.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(windowDuration: TimeInterval, overlapFactor: Double)
```

## Parameters

- `windowDuration`: The window duration in seconds. The window duration should be greater than or equal to 0.5 seconds and less than or equal to   15.0 seconds.
- `overlapFactor`: The overlap factor. The overlap should be greater than or equal to zero and less than one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/audiofeatureprint/init(windowduration:overlapfactor:))*