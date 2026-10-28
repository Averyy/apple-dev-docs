# latestTimeTravelDate

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The latest date supported by Time Travel.

**Availability**:
- watchOS 2.0+ - Deprecated in 7.0

> **Deprecated**: Time Travel is no longer supported.

## Declaration

```swift
var latestTimeTravelDate: Date { get }
```

```objc
@property (nonatomic, readonly) NSDate * latestTimeTravelDate;
```

## Discussion

When constructing your timeline, don’t create any entries after this date. Doing so is a waste of time because those entries won’t be displayed right away.

## See Also

### Getting the Time Travel Boundaries
- [var earliestTimeTravelDate: Date](./earliesttimetraveldate.md)
  The earliest Time Travel date for which you should provide data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationserver/latesttimetraveldate)*