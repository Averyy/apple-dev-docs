# initWithIdentifier:displayName:supportedFamilies:

**Framework**: ClockKit  
**Kind**: method  
**Role**: Instance Method

Returns a new complication descriptor.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```objc
- (instancetype) initWithIdentifier:(NSString *) identifier displayName:(NSString *) displayName supportedFamilies:(NSArray<NSNumber *> *) supportedFamilies;
```

## Parameters

- `identifier`: A string that uniquely identifies the descriptor.
- `displayName`: A localized name that ClockKit shows to the user to identify complications from the descriptor.
- `supportedFamilies`: The families that support this type of complication. Note that different descriptors can support different sets of families.

## See Also

### Creating descriptors
- [- initWithIdentifier:displayName:supportedFamilies:userActivity:](./initwithidentifier_displayname_supportedfamilies_useractivity_.md)
  Returns a new complication descriptor with an associated user activity.
- [- initWithIdentifier:displayName:supportedFamilies:userInfo:](./initwithidentifier_displayname_supportedfamilies_userinfo_.md)
  Returns a new complication descriptor with an associated user info dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationdescriptor/initwithidentifier:displayname:supportedfamilies:)*