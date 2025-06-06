# supportedFamilies

**Framework**: ClockKit  
**Kind**: property

The families that support this type of complication.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
var supportedFamilies: [CLKComplicationFamily] { get }
```

#### Discussion

Different descriptors can support different sets of families.

## See Also

- [var identifier: String](clkcomplicationdescriptor/identifier.md)
  A string that uniquely identifies the descriptor.
- [var displayName: String](clkcomplicationdescriptor/displayname.md)
  A localized string that identifies complications from the descriptor to the user.
- [var userActivity: NSUserActivity?](clkcomplicationdescriptor/useractivity.md)
  A user activity object that represents the state of the app at a moment in time.
- [var userInfo: [AnyHashable : Any]?](clkcomplicationdescriptor/userinfo.md)
  A dictionary of data that your data source can use to generate timeline entries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationdescriptor/supportedfamilies-4ckbx)*