# init(timeIntervalSinceNow:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns a date object initialized relative to the current date and time by a given number of seconds.

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
convenience init(timeIntervalSinceNow secs: TimeInterval)
```

```objc
- (instancetype) initWithTimeIntervalSinceNow:(NSTimeInterval) secs;
```

#### Return Value

An `NSDate` object initialized relative to the current date and time by `secs` seconds.

## Parameters

- `secs`: The number of seconds from relative to the current date and time to which the receiver should be initialized. A negative value means the returned object will represent a date in the past.

## See Also

### Initializing a Date
- [init()](./init%28%29.md)
  Returns a date object initialized to the current date and time.
- [init(timeIntervalSinceReferenceDate: TimeInterval)](./init%28timeintervalsincereferencedate%29.md)
  Returns a date object initialized relative to 00:00:00 UTC on 1 January 2001 by a given number of seconds.
- [convenience init(timeIntervalSince1970: TimeInterval)](./init%28timeintervalsince1970%29.md)
  Returns a date object initialized relative to 00:00:00 UTC on 1 January 1970 by a given number of seconds.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Returns a date object initialized from data in the given unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdate/init(timeintervalsincenow:))*