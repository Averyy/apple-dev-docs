# init()

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns a date object initialized to the current date and time.

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
init()
```

```objc
- (instancetype) init;
```

#### Return Value

An `NSDate` object initialized to the current date and time.

#### Discussion

This method is a designated initializer for `NSDate`.

## See Also

### Initializing a Date
- [convenience init(timeIntervalSinceNow: TimeInterval)](./init%28timeintervalsincenow%29.md)
  Returns a date object initialized relative to the current date and time by a given number of seconds.
- [init(timeIntervalSinceReferenceDate: TimeInterval)](./init%28timeintervalsincereferencedate%29.md)
  Returns a date object initialized relative to 00:00:00 UTC on 1 January 2001 by a given number of seconds.
- [convenience init(timeIntervalSince1970: TimeInterval)](./init%28timeintervalsince1970%29.md)
  Returns a date object initialized relative to 00:00:00 UTC on 1 January 1970 by a given number of seconds.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Returns a date object initialized from data in the given unarchiver.
### Related Documentation
- [+ date](./date.md)
  Creates and returns a new date object set to the current date and time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdate/init())*