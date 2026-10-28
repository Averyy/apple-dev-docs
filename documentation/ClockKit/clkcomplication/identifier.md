# identifier

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

An identifier that specifies a complication if your app supports multiple complications per family.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```swift
var identifier: String { get }
```

```objc
@property (nonatomic, readonly) NSString * identifier;
```

## Mentions

- [Creating a timeline entry](../creating-a-timeline-entry.md)

## Discussion

In watchOS 7 and later, ClockKit represents a complication by its [`family`](./family.md) and its [`CLKComplicationDescriptor`](../clkcomplicationdescriptor.md). Descriptors often represent categories of information that the complication can display. For example, a weather app may support `Condition`, `Temperature`, and `Precipitation` descriptors.

```swift
let ComplicationConditionIdentifier = "ComplicationTypeCondition"
let ComplicationTemperatureIdentifier = "ComplicationTypeTemperature"
let ComplicationPrecipitationPercentageIdentifier = "ComplicationTypePrecipitationPercentage"
```

For apps created for watchOS 6 or earlier, the system automatically sets the configuration’s [`identifier`](./identifier.md) property to [`CLKDefaultComplicationIdentifier`](../clkdefaultcomplicationidentifier.md) if you don’t implement your data source’s [`getComplicationDescriptors(handler:)`](../clkcomplicationdatasource/getcomplicationdescriptors%28handler%29.md) method. Similarly, the system sets the identifier to [`CLKDefaultComplicationIdentifier`](../clkdefaultcomplicationidentifier.md) if the complication came from a shared watch face, but the sender chose to exclude private information.

Because default identifiers can come from shared watch faces, your data source’s [`getCurrentTimelineEntry(for:withHandler:)`](../clkcomplicationdatasource/getcurrenttimelineentry%28for,withhandler%29.md) and [`getTimelineEntries(for:after:limit:withHandler:)`](../clkcomplicationdatasource/gettimelineentries%28for,after,limit,withhandler%29.md) methods must check for the [`CLKDefaultComplicationIdentifier`](../clkdefaultcomplicationidentifier.md) value, and provide generic complication entries when it occurs.

## See Also

### Accessing Data About the Complication
- [var family: CLKComplicationFamily](./family.md)
  The family to which the complication belongs.
- [var userActivity: NSUserActivity?](./useractivity.md)
  An object that represents the state of the app at a moment in time.
- [var userInfo: [AnyHashable : Any]?](./userinfo.md)
  A dictionary of additional data associated with the complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplication/identifier)*