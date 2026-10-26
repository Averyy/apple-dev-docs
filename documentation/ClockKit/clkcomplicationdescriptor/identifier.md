# identifier

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

A string that uniquely identifies the descriptor.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
var identifier: String { get }
```

```objc
@property (nonatomic, readonly) NSString * identifier;
```

## See Also

### Accessing the descriptor’s data
- [var displayName: String](./displayname.md)
  A localized string that identifies complications from the descriptor to the user.
- [var supportedFamilies: [CLKComplicationFamily]](./supportedfamilies-4ckbx.md)
  The families that support this type of complication.
- [var userActivity: NSUserActivity?](./useractivity.md)
  A user activity object that represents the state of the app at a moment in time.
- [var userInfo: [AnyHashable : Any]?](./userinfo.md)
  A dictionary of data that your data source can use to generate timeline entries.
- [supportedFamilies](./supportedfamilies-50ink.md)
  The families that support this type of complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationdescriptor/identifier)*