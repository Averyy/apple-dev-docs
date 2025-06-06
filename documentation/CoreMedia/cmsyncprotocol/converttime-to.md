# convertTime(_:to:)

**Framework**: Core Media  
**Kind**: method  
**Required**: Yes

Converts a time from one timebase or clock to another timebase or clock.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func convertTime<T>(_ time: CMTime, to clockOrTimebase: T) -> CMTime where T : CMSyncProtocol
```

## Parameters

- `time`: The time to convert from.
- `clockOrTimebase`: The clock or time to convert to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsyncprotocol/converttime(_:to:))*