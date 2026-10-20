# displayName

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

A localized string that identifies complications from the descriptor to the user.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
var displayName: String { get }
```

```objc
@property (nonatomic, readonly) NSString * displayName;
```

## See Also

### Accessing the descriptor’s data
- [var identifier: String](./identifier.md)
  A string that uniquely identifies the descriptor.
- [var supportedFamilies: [CLKComplicationFamily]](./supportedfamilies-4ckbx.md)
  The families that support this type of complication.
- [var userActivity: NSUserActivity?](./useractivity.md)
  A user activity object that represents the state of the app at a moment in time.
- [var userInfo: [AnyHashable : Any]?](./userinfo.md)
  A dictionary of data that your data source can use to generate timeline entries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationdescriptor/displayname)*