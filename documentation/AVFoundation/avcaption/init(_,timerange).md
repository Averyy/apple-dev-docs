# init(_:timeRange:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates a caption that contains text and a time range.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
init(_ text: String, timeRange: CMTimeRange)
```

```objc
- (instancetype) initWithText:(NSString *) text timeRange:(CMTimeRange) timeRange;
```

## Parameters

- `text`: The text the caption displays.
- `timeRange`: The range of time when the caption is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaption/init(_:timerange:))*