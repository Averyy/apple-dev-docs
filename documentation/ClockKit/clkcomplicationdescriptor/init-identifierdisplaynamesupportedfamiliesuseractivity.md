# init(identifier:displayName:supportedFamilies:userActivity:)

**Framework**: ClockKit  
**Kind**: init

Returns a new complication descriptor with an associated user activity.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
convenience init(identifier: String, displayName: String, supportedFamilies: [CLKComplicationFamily], userActivity: NSUserActivity)
```

## Mentions

- [Declaring complications for your app](declaring-complications-for-your-app.md)

#### Discussion

If the user taps on a complication specified by this descriptor, the system launches the app and calls [`handle(_:)`](https://developer.apple.com/documentation/WatchKit/WKExtensionDelegate/handle(_:)-5pyj1), passing the user activity. Your [`handle(_:)`](https://developer.apple.com/documentation/WatchKit/WKExtensionDelegate/handle(_:)-5pyj1) method should update the app so that it’s in the specified state.

Because the system can pass configurations as part of a shared watch face, only include data useable by any instance of the app. For example, avoid using identifiers that might change between users, like an index into the user’s favorites list. Instead, use items that remain constant across all copies of the app, like unique string identifiers.

## Parameters

- `identifier`: A string that uniquely identifies the descriptor.
- `displayName`: A localized name that ClockKit shows to the user to identify complications from the descriptor.
- `supportedFamilies`: The families that support this type of complication. Note that different descriptors can support different sets of families.
- `userActivity`: A user activity object that represents the state of the app at a moment in time.

## See Also

- [convenience init(identifier: String, displayName: String, supportedFamilies: [CLKComplicationFamily])](clkcomplicationdescriptor/init(identifier:displayname:supportedfamilies:).md)
  Returns a new complication descriptor.
- [convenience init(identifier: String, displayName: String, supportedFamilies: [CLKComplicationFamily], userInfo: [AnyHashable : Any])](clkcomplicationdescriptor/init(identifier:displayname:supportedfamilies:userinfo:).md)
  Returns a new complication descriptor with an associated dictionary of user data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationdescriptor/init(identifier:displayname:supportedfamilies:useractivity:))*