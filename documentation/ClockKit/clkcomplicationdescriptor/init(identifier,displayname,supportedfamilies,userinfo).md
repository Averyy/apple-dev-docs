# init(identifier:displayName:supportedFamilies:userInfo:)

**Framework**: ClockKit  
**Kind**: init  
**Role**: Initializer

Returns a new complication descriptor with an associated dictionary of user data.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
convenience init(identifier: String, displayName: String, supportedFamilies: [CLKComplicationFamily], userInfo: [AnyHashable : Any])
```

## Mentions

- [Declaring complications for your app](../declaring-complications-for-your-app.md)

#### Discussion

The system passes the user info dictionary to methods like your data source’s [`getCurrentTimelineEntry(for:withHandler:)`](../clkcomplicationdatasource/getcurrenttimelineentry%28for,withhandler%29.md) method as part of the complication. Your data source can use the information in the user info dictionary when creating the complications.

Because the system can pass configurations as part of a shared watch face, only include data in the user info dictionary that any instance of the app can use. For example, avoid using identifiers that might change between users, like an index into the user’s favorites list. Instead, use items that remain constant across all copies of the app, like unique string identifiers.

When the user taps your complication, ClockKit includes the content of the `userInfo` property in the dictionary passed to the extension delegate’s [`handleUserActivity(_:)`](../../WatchKit/wkextensiondelegate/handleuseractivity%28_%29.md) method.

## Parameters

- `identifier`: A string that uniquely identifies the descriptor.
- `displayName`: A localized name that ClockKit shows to the user to identify complications from the descriptor.
- `supportedFamilies`: The families that support this type of complication. Note that different descriptors can support different sets of families.
- `userInfo`: A dictionary containing additional data that helps your complication data source generate timeline entries.

## See Also

### Creating descriptors
- [convenience init(identifier: String, displayName: String, supportedFamilies: [CLKComplicationFamily])](./init%28identifier,displayname,supportedfamilies%29.md)
  Returns a new complication descriptor.
- [convenience init(identifier: String, displayName: String, supportedFamilies: [CLKComplicationFamily], userActivity: NSUserActivity)](./init%28identifier,displayname,supportedfamilies,useractivity%29.md)
  Returns a new complication descriptor with an associated user activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationdescriptor/init(identifier:displayname:supportedfamilies:userinfo:))*