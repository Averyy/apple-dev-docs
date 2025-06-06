# earliestTimeTravelDate

**Framework**: ClockKit  
**Kind**: property

The earliest Time Travel date for which you should provide data.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var earliestTimeTravelDate: Date { get }
```

#### Discussion

When constructing your timeline, don’t create any entries before this date. Doing so is a waste of time because those entries will never be displayed.

## See Also

- [var latestTimeTravelDate: Date](clkcomplicationserver/latesttimetraveldate.md)
  The latest date supported by Time Travel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationserver/earliesttimetraveldate)*