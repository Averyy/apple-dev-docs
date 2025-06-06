# latestTimeTravelDate

**Framework**: ClockKit  
**Kind**: property

The latest date supported by Time Travel.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var latestTimeTravelDate: Date { get }
```

#### Discussion

When constructing your timeline, don’t create any entries after this date. Doing so is a waste of time because those entries won’t be displayed right away.

## See Also

- [var earliestTimeTravelDate: Date](clkcomplicationserver/earliesttimetraveldate.md)
  The earliest Time Travel date for which you should provide data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationserver/latesttimetraveldate)*