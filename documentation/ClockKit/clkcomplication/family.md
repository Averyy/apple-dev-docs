# family

**Framework**: ClockKit  
**Kind**: property

The family to which the complication belongs.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var family: CLKComplicationFamily { get }
```

## Mentions

- [Creating a timeline entry](creating-a-timeline-entry.md)

#### Discussion

The [`family`](clkcomplication/family.md) property determines how much space is available to a complication and which templates you can use to display your complication data. In your complication data source, you typically use the property’s value in a `switch` statement when determining the complication template your data source creates.

In watchOS 7 and later, ClockKit represents complications using its [`family`](clkcomplication/family.md) and [`identifier`](clkcomplication/identifier.md). Each pair represents a unique complication that the user can select.

In watchOS 6 and earlier, ClockKit represents a complication by its [`family`](clkcomplication/family.md) only. Each family can only have one complication. For more information, see [`Declaring complications for your app`](declaring-complications-for-your-app.md).

## See Also

- [var identifier: String](clkcomplication/identifier.md)
  An identifier that specifies a complication if your app supports multiple complications per family.
- [var userActivity: NSUserActivity?](clkcomplication/useractivity.md)
  An object that represents the state of the app at a moment in time.
- [var userInfo: [AnyHashable : Any]?](clkcomplication/userinfo.md)
  A dictionary of additional data associated with the complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplication/family)*