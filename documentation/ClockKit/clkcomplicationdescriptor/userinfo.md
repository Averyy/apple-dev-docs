# userInfo

**Framework**: ClockKit  
**Kind**: property

A dictionary of data that your data source can use to generate timeline entries.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
var userInfo: [AnyHashable : Any]? { get }
```

#### Discussion

The system passes the user info dictionary to methods like your data source’s [`getCurrentTimelineEntry(for:withHandler:)`](clkcomplicationdatasource/getcurrenttimelineentry(for:withhandler:).md) method as part of the complication. Your data source can use the information in the user info dictionary when creating these complications.

Because the system can pass configurations as part of a shared watch face, only include data in the user info dictionary that any instance of the app can use. For example, avoid using identifiers that might change between users, like an index into the user’s favorites list. Instead, use items that remain constant across all copies of the app, like unique string identifiers.

When the user taps your complication, ClockKit includes the content of the `userInfo` property in the dictionary passed to the extension delegate’s [`handleUserActivity(_:)`](https://developer.apple.com/documentation/WatchKit/WKExtensionDelegate/handleUserActivity(_:)) method.

## See Also

- [var identifier: String](clkcomplicationdescriptor/identifier.md)
  A string that uniquely identifies the descriptor.
- [var displayName: String](clkcomplicationdescriptor/displayname.md)
  A localized string that identifies complications from the descriptor to the user.
- [var supportedFamilies: [CLKComplicationFamily]](clkcomplicationdescriptor/supportedfamilies-4ckbx.md)
  The families that support this type of complication.
- [var userActivity: NSUserActivity?](clkcomplicationdescriptor/useractivity.md)
  A user activity object that represents the state of the app at a moment in time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationdescriptor/userinfo)*