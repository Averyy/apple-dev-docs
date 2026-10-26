# activityMoveMode()

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Returns the activity move mode for the current user.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func activityMoveMode() throws -> HKActivityMoveModeObject
```

```objc
- (HKActivityMoveModeObject *) activityMoveModeWithError:(NSError **) error;
```

## See Also

### Accessing the move mode
- [static let HKUserPreferencesDidChange: NSNotification.Name](../../Foundation/nsnotification/name-swift.struct/hkuserpreferencesdidchange.md)
  Notifies observers whenever the user changes his or her preferred units.
- [HKUserPreferencesDidChangeNotification](../hkuserpreferencesdidchangenotification.md)
  Notifies observers whenever the user changes his or her preferred units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/activitymovemode())*