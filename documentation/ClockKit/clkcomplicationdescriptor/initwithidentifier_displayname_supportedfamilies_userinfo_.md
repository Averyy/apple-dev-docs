# initWithIdentifier:displayName:supportedFamilies:userInfo:

**Framework**: ClockKit  
**Kind**: method  
**Role**: Instance Method

Returns a new complication descriptor with an associated user info dictionary.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```objc
- (instancetype) initWithIdentifier:(NSString *) identifier displayName:(NSString *) displayName supportedFamilies:(NSArray<NSNumber *> *) supportedFamilies userInfo:(NSDictionary *) userInfo;
```

## Discussion

The system passes the user info dictionary to methods like your data source’s [`getCurrentTimelineEntry(for:withHandler:)`](../clkcomplicationdatasource/getcurrenttimelineentry%28for,withhandler%29.md) method as part of the complication. Your data source can use the information in the user info dictionary when creating the complications.

Because the system can pass configurations as part of a shared watch face, only include data in the user info dictionary that any instance of the app can use. For example, avoid using identifiers that might change between users, like an index into the user’s favorites list. Instead, use items that remain constant across all copies of the app, like unique string identifiers.

When the user taps your complication, ClockKit includes the content of the `userInfo` property in the dictionary passed to the extension delegate’s [`handleUserActivity(_:)`](../../WatchKit/wkextensiondelegate/handleuseractivity%28_%29.md) method.

## Parameters

- `identifier`: A string that uniquely identifies the descriptor.
- `displayName`: A localized name that ClockKit shows to the user to identify complications from the descriptor.
- `supportedFamilies`: The families that support this type of complication. Note that different descriptors can support different sets of families.
- `userInfo`: A dictionary containing additional data that helps your complication data source generate timeline entries.

## See Also

### Creating descriptors
- [- initWithIdentifier:displayName:supportedFamilies:](./initwithidentifier_displayname_supportedfamilies_.md)
  Returns a new complication descriptor.
- [- initWithIdentifier:displayName:supportedFamilies:userActivity:](./initwithidentifier_displayname_supportedfamilies_useractivity_.md)
  Returns a new complication descriptor with an associated user activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationdescriptor/initwithidentifier:displayname:supportedfamilies:userinfo:)*