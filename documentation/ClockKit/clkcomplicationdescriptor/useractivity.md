# userActivity

**Framework**: ClockKit  
**Kind**: property

A user activity object that represents the state of the app at a moment in time.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
var userActivity: NSUserActivity? { get }
```

#### Discussion

When the user taps on a complication specified by this configuration, the system launches the app and calls [`handle(_:)`](https://developer.apple.com/documentation/WatchKit/WKExtensionDelegate/handle(_:)-5pyj1), passing the user activity. Your extension delegate’s handle method should update the app so that it’s in the specified state.

Because the system can pass configurations as part of a shared watch face, only include data useable by any instance of the app. For example, avoid using identifiers that might change between users, like an index into the user’s favorites list. Instead, use items that remain constant across all copies of the app, like unique string identifiers.

## See Also

- [var identifier: String](clkcomplicationdescriptor/identifier.md)
  A string that uniquely identifies the descriptor.
- [var displayName: String](clkcomplicationdescriptor/displayname.md)
  A localized string that identifies complications from the descriptor to the user.
- [var supportedFamilies: [CLKComplicationFamily]](clkcomplicationdescriptor/supportedfamilies-4ckbx.md)
  The families that support this type of complication.
- [var userInfo: [AnyHashable : Any]?](clkcomplicationdescriptor/userinfo.md)
  A dictionary of data that your data source can use to generate timeline entries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationdescriptor/useractivity)*