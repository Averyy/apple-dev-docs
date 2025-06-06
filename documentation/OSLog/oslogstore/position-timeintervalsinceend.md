# position(timeIntervalSinceEnd:)

**Framework**: OSLog  
**Kind**: method

Returns a position representing time since the end of the time range that the entries span.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func position(timeIntervalSinceEnd seconds: TimeInterval) -> OSLogPosition
```

## See Also

- [func position(date: Date) -> OSLogPosition](oslogstore/position(date:).md)
  Returns a position representing the time specified.
- [func position(timeIntervalSinceLatestBoot: TimeInterval) -> OSLogPosition](oslogstore/position(timeintervalsincelatestboot:).md)
  Returns a position representing time since the last boot in the series of entries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/oslog/oslogstore/position(timeintervalsinceend:))*