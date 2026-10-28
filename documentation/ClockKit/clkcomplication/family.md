# family

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The family to which the complication belongs.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
var family: CLKComplicationFamily { get }
```

```objc
@property (nonatomic, readonly) CLKComplicationFamily family;
```

## Mentions

- [Creating a timeline entry](../creating-a-timeline-entry.md)

## Discussion

The [`family`](./family.md) property determines how much space is available to a complication and which templates you can use to display your complication data. In your complication data source, you typically use the property’s value in a `switch` statement when determining the complication template your data source creates.

In watchOS 7 and later, ClockKit represents complications using its [`family`](./family.md) and [`identifier`](./identifier.md). Each pair represents a unique complication that the user can select.

In watchOS 6 and earlier, ClockKit represents a complication by its [`family`](./family.md) only. Each family can only have one complication. For more information, see [Declaring complications for your app](../declaring-complications-for-your-app.md).

## See Also

### Accessing Data About the Complication
- [var identifier: String](./identifier.md)
  An identifier that specifies a complication if your app supports multiple complications per family.
- [var userActivity: NSUserActivity?](./useractivity.md)
  An object that represents the state of the app at a moment in time.
- [var userInfo: [AnyHashable : Any]?](./userinfo.md)
  A dictionary of additional data associated with the complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplication/family)*