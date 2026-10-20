# position(timeIntervalSinceLatestBoot:)

**Framework**: OSLog  
**Kind**: method  
**Role**: Instance Method

Returns a position representing time since the last boot in the series of entries.

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
func position(timeIntervalSinceLatestBoot seconds: TimeInterval) -> OSLogPosition
```

```objc
- (OSLogPosition *) positionWithTimeIntervalSinceLatestBoot:(NSTimeInterval) seconds;
```

## See Also

### Accessing Position
- [func position(date: Date) -> OSLogPosition](./position%28date%29.md)
  Returns a position representing the time specified.
- [func position(timeIntervalSinceEnd: TimeInterval) -> OSLogPosition](./position%28timeintervalsinceend%29.md)
  Returns a position representing time since the end of the time range that the entries span.


---

*[View on Apple Developer](https://developer.apple.com/documentation/oslog/oslogstore/position(timeintervalsincelatestboot:))*