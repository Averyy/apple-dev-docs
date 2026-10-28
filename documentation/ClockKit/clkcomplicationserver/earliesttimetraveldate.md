# earliestTimeTravelDate

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The earliest Time Travel date for which you should provide data.

**Availability**:
- watchOS 2.0+ - Deprecated in 7.0

> **Deprecated**: Time Travel is no longer supported.

## Declaration

```swift
var earliestTimeTravelDate: Date { get }
```

```objc
@property (nonatomic, readonly) NSDate * earliestTimeTravelDate;
```

## Discussion

When constructing your timeline, don’t create any entries before this date. Doing so is a waste of time because those entries will never be displayed.

## See Also

### Getting the Time Travel Boundaries
- [var latestTimeTravelDate: Date](./latesttimetraveldate.md)
  The latest date supported by Time Travel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationserver/earliesttimetraveldate)*