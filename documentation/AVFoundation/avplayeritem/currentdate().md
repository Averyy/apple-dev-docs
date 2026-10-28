# currentDate()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns the current time of the item as a date.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
nonisolated
func currentDate() -> Date?
```

```objc
- (NSDate *) currentDate;
```

## Return Value

The current time of the item as a date, or `nil` if there isn’t a mapped date for the item.

## Discussion

The system calculates this value from the `EXT-X-PROGRAM-DATE-TIME` tag.

## See Also

### Accessing timing information
- [func currentTime() -> CMTime](./currenttime%28%29.md)
  Returns the current time of the item.
- [var duration: CMTime](./duration.md)
  The duration of the item.
- [var timebase: CMTimebase?](./timebase.md)
  The timebase information for the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/currentdate())*