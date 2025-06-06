# userInfo

**Framework**: ClockKit  
**Kind**: property

A dictionary of additional data associated with the complication.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
var userInfo: [AnyHashable : Any]? { get }
```

## Mentions

- [Sharing an Apple Watch face](sharing-an-apple-watch-face.md)
- [Creating a timeline entry](creating-a-timeline-entry.md)

#### Discussion

Because the system can pass configurations as part of a shared watch face, only include data in the user info dictionary that any instance of the app can use. For example, avoid using identifiers that might change between users, like an index into the user’s favorites list. Instead, use items that remain constant across all copies of the app, like unique string identifiers.

When the user taps your complication, ClockKit includes the content of the `userInfo` property in the dictionary passed to the extension delegate’s [`handleUserActivity(_:)`](https://developer.apple.com/documentation/WatchKit/WKExtensionDelegate/handleUserActivity(_:)) method. Your data source can also access the user info dictionary when creating the template for this complication.

## See Also

- [var family: CLKComplicationFamily](clkcomplication/family.md)
  The family to which the complication belongs.
- [var identifier: String](clkcomplication/identifier.md)
  An identifier that specifies a complication if your app supports multiple complications per family.
- [var userActivity: NSUserActivity?](clkcomplication/useractivity.md)
  An object that represents the state of the app at a moment in time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplication/userinfo)*