# userInfo

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

A dictionary of additional data associated with the complication.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```swift
var userInfo: [AnyHashable : Any]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSDictionary * userInfo;
```

## Mentions

- [Creating a timeline entry](../creating-a-timeline-entry.md)
- [Sharing an Apple Watch face](../sharing-an-apple-watch-face.md)

## Discussion

Because the system can pass configurations as part of a shared watch face, only include data in the user info dictionary that any instance of the app can use. For example, avoid using identifiers that might change between users, like an index into the user’s favorites list. Instead, use items that remain constant across all copies of the app, like unique string identifiers.

When the user taps your complication, ClockKit includes the content of the `userInfo` property in the dictionary passed to the extension delegate’s [`handleUserActivity(_:)`](../../WatchKit/wkextensiondelegate/handleuseractivity%28_%29.md) method. Your data source can also access the user info dictionary when creating the template for this complication.

## See Also

### Accessing Data About the Complication
- [var family: CLKComplicationFamily](./family.md)
  The family to which the complication belongs.
- [var identifier: String](./identifier.md)
  An identifier that specifies a complication if your app supports multiple complications per family.
- [var userActivity: NSUserActivity?](./useractivity.md)
  An object that represents the state of the app at a moment in time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplication/userinfo)*