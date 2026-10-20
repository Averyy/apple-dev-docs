# preservesRepeatMode

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the chosen repeat mode is preserved between playback sessions.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 8.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var preservesRepeatMode: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL preservesRepeatMode;
```

#### Discussion

When set to [`true`](../../Swift/true.md), the chosen repeat mode is preserved between playback sessions.

## See Also

### Changing the repeat type
- [var repeatType: MPRepeatType](./repeattype.md)
  The repeat type used when fulfilling the event request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpchangerepeatmodecommandevent/preservesrepeatmode)*