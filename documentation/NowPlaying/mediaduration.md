# MediaDuration

**Framework**: Now Playing  
**Kind**: enum

The duration of media content.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
enum MediaDuration
```

#### Overview

Use this enumeration to specify whether content has a finite duration or is a live stream without a defined end time.

## Topics

### Enumeration Cases
- [MediaDuration.continuous](mediaduration/continuous.md)
  Content with no defined duration that isn’t a live broadcast.
- [case finite(TimeInterval)](mediaduration/finite(_:).md)
  Content with a known duration.
- [MediaDuration.live](mediaduration/live.md)
  Live or streaming content without a defined duration.

## See Also

- [enum MediaType](mediatype.md)
  The type of media being played.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediaduration)*