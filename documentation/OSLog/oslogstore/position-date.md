# position(date:)

**Framework**: OSLog  
**Kind**: method

Returns a position representing the time specified.

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
func position(date: Date) -> OSLogPosition
```

#### Discussion

If there are multiple occurrences of the same time, the method returns the earliest occurrence.

## See Also

- [func position(timeIntervalSinceEnd: TimeInterval) -> OSLogPosition](oslogstore/position(timeintervalsinceend:).md)
  Returns a position representing time since the end of the time range that the entries span.
- [func position(timeIntervalSinceLatestBoot: TimeInterval) -> OSLogPosition](oslogstore/position(timeintervalsincelatestboot:).md)
  Returns a position representing time since the last boot in the series of entries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/oslog/oslogstore/position(date:))*