# duration

**Framework**: AVFoundation  
**Kind**: property

A time value that indicates the asset’s duration.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var duration: CMTime { get }
```

#### Discussion

If you initialized the asset by passing the [`AVURLAssetPreferPreciseDurationAndTimingKey`](avurlassetpreferprecisedurationandtimingkey.md) initialization option, this property value provides the asset’s precise duration; otherwise, it provides a best-available estimate. You can determine the value’s accuracy by querying the asset’s [`providesPreciseDurationAndTiming`](avasset/providesprecisedurationandtiming.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/duration)*