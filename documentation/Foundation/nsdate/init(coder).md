# init(coder:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns a date object initialized from data in the given unarchiver.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(coder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) coder;
```

## See Also

### Initializing a Date
- [init()](./init%28%29.md)
  Returns a date object initialized to the current date and time.
- [convenience init(timeIntervalSinceNow: TimeInterval)](./init%28timeintervalsincenow%29.md)
  Returns a date object initialized relative to the current date and time by a given number of seconds.
- [init(timeIntervalSinceReferenceDate: TimeInterval)](./init%28timeintervalsincereferencedate%29.md)
  Returns a date object initialized relative to 00:00:00 UTC on 1 January 2001 by a given number of seconds.
- [convenience init(timeIntervalSince1970: TimeInterval)](./init%28timeintervalsince1970%29.md)
  Returns a date object initialized relative to 00:00:00 UTC on 1 January 1970 by a given number of seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdate/init(coder:))*