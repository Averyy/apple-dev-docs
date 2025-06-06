# init(identifier:displayName:supportedFamilies:)

**Framework**: ClockKit  
**Kind**: init

Returns a new complication descriptor.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
convenience init(identifier: String, displayName: String, supportedFamilies: [CLKComplicationFamily])
```

## Parameters

- `identifier`: A string that uniquely identifies the descriptor.
- `displayName`: A localized name that ClockKit shows to the user to identify complications from the descriptor.
- `supportedFamilies`: The families that support this type of complication. Note that different descriptors can support different sets of families.

## See Also

- [convenience init(identifier: String, displayName: String, supportedFamilies: [CLKComplicationFamily], userActivity: NSUserActivity)](clkcomplicationdescriptor/init(identifier:displayname:supportedfamilies:useractivity:).md)
  Returns a new complication descriptor with an associated user activity.
- [convenience init(identifier: String, displayName: String, supportedFamilies: [CLKComplicationFamily], userInfo: [AnyHashable : Any])](clkcomplicationdescriptor/init(identifier:displayname:supportedfamilies:userinfo:).md)
  Returns a new complication descriptor with an associated dictionary of user data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationdescriptor/init(identifier:displayname:supportedfamilies:))*