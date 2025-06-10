# frame(at:tolerance:)

**Framework**: Cinematic  
**Kind**: method

The closest frame to the given time within the given tolerance.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
final func frame(at time: CMTime, tolerance: CMTime) -> CNScript.Frame?
```

#### Return Value

The closest frame to the time of interest within the given tolerance.

## Parameters

- `time`: The time of interest.
- `tolerance`: The tolerance time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnscript-1ispe/frame(at:tolerance:))*