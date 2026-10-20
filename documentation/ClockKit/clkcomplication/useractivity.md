# userActivity

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

An object that represents the state of the app at a moment in time.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```swift
var userActivity: NSUserActivity? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSUserActivity * userActivity;
```

## Mentions

- [Sharing an Apple Watch face](../sharing-an-apple-watch-face.md)

#### Discussion

When the user taps on a complication specified by this configuration, the system launches the app and calls [`handle(_:)`](../../WatchKit/wkextensiondelegate/handle%28_%29-5pyj1.md), passing the user activity. Your extension delegate’s [`handle(_:)`](../../WatchKit/wkextensiondelegate/handle%28_%29-5pyj1.md) method should update the app so that it’s in the specified state.

Because the system can pass configurations as part of a shared watch face, only include data useable by any instance of the app. For example, avoid using identifiers that might change between users, like an index into the user’s favorites list. Instead, use items that remain constant across all copies of the app, like unique string identifiers.

## See Also

### Accessing Data About the Complication
- [var family: CLKComplicationFamily](./family.md)
  The family to which the complication belongs.
- [var identifier: String](./identifier.md)
  An identifier that specifies a complication if your app supports multiple complications per family.
- [var userInfo: [AnyHashable : Any]?](./userinfo.md)
  A dictionary of additional data associated with the complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplication/useractivity)*