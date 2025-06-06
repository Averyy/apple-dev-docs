# userActivity

**Framework**: ClockKit  
**Kind**: property

An object that represents the state of the app at a moment in time.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
var userActivity: NSUserActivity? { get }
```

## Mentions

- [Sharing an Apple Watch face](sharing-an-apple-watch-face.md)

#### Discussion

When the user taps on a complication specified by this configuration, the system launches the app and calls [`handle(_:)`](https://developer.apple.com/documentation/WatchKit/WKExtensionDelegate/handle(_:)-5pyj1), passing the user activity. Your extension delegate’s [`handle(_:)`](https://developer.apple.com/documentation/WatchKit/WKExtensionDelegate/handle(_:)-5pyj1) method should update the app so that it’s in the specified state.

Because the system can pass configurations as part of a shared watch face, only include data useable by any instance of the app. For example, avoid using identifiers that might change between users, like an index into the user’s favorites list. Instead, use items that remain constant across all copies of the app, like unique string identifiers.

## See Also

- [var family: CLKComplicationFamily](clkcomplication/family.md)
  The family to which the complication belongs.
- [var identifier: String](clkcomplication/identifier.md)
  An identifier that specifies a complication if your app supports multiple complications per family.
- [var userInfo: [AnyHashable : Any]?](clkcomplication/userinfo.md)
  A dictionary of additional data associated with the complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplication/useractivity)*