# currentDate()

**Framework**: AVFoundation  
**Kind**: method

Returns the current time of the item as a date.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
nonisolated
func currentDate() -> Date?
```

#### Return Value

The current time of the item as a date, or `nil` if there isn’t a mapped date for the item.

#### Discussion

The system calculates this value from the `EXT-X-PROGRAM-DATE-TIME` tag.

## See Also

- [func currentTime() -> CMTime](avplayeritem/currenttime.md)
  Returns the current time of the item.
- [var duration: CMTime](avplayeritem/duration.md)
  The duration of the item.
- [var timebase: CMTimebase?](avplayeritem/timebase.md)
  The timebase information for the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/currentdate())*