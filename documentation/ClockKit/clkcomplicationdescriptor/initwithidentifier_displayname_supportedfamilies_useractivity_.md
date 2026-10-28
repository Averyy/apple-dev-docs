# initWithIdentifier:displayName:supportedFamilies:userActivity:

**Framework**: ClockKit  
**Kind**: method  
**Role**: Instance Method

Returns a new complication descriptor with an associated user activity.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```objc
- (instancetype) initWithIdentifier:(NSString *) identifier displayName:(NSString *) displayName supportedFamilies:(NSArray<NSNumber *> *) supportedFamilies userActivity:(NSUserActivity *) userActivity;
```

## Discussion

If the user taps on a complication specified by this descriptor, the system launches the app and calls [`handle(_:)`](../../WatchKit/wkextensiondelegate/handle%28_%29-5pyj1.md), passing the user activity. Your [`handle(_:)`](../../WatchKit/wkextensiondelegate/handle%28_%29-5pyj1.md) method should update the app so that it’s in the specified state.

Because the system can pass configurations as part of a shared watch face, only include data useable by any instance of the app. For example, avoid using identifiers that might change between users, like an index into the user’s favorites list. Instead, use items that remain constant across all copies of the app, like unique string identifiers.

## Parameters

- `identifier`: A string that uniquely identifies the descriptor.
- `displayName`: A localized name that ClockKit shows to the user to identify complications from the descriptor.
- `supportedFamilies`: The families that support this type of complication. Note that different descriptors can support different sets of families.
- `userActivity`: A user activity object that represents the state of the app at a moment in time.

## See Also

### Creating descriptors
- [- initWithIdentifier:displayName:supportedFamilies:](./initwithidentifier_displayname_supportedfamilies_.md)
  Returns a new complication descriptor.
- [- initWithIdentifier:displayName:supportedFamilies:userInfo:](./initwithidentifier_displayname_supportedfamilies_userinfo_.md)
  Returns a new complication descriptor with an associated user info dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationdescriptor/initwithidentifier:displayname:supportedfamilies:useractivity:)*