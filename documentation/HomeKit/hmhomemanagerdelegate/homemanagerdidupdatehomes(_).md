# homeManagerDidUpdateHomes(_:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the home manager updated its collection of homes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func homeManagerDidUpdateHomes(_ manager: HMHomeManager)
```

```objc
- (void) homeManagerDidUpdateHomes:(HMHomeManager *) manager;
```

## Discussion

The home manager calls this method to inform an application of significant changes to the home configuration, including when the manager finishes its first load of data from the HomeKit database on initialization. Use this method as a cue to invalidate any references to HomeKit objects and refresh your app’s views with the new list of homes.

## Parameters

- `manager`: The home manager with updated homes.

## See Also

### Adding and removing homes
- [func homeManager(HMHomeManager, didAdd: HMHome)](./homemanager%28_,didadd%29.md)
  Tells the delegate that the home manager added a home.
- [func homeManager(HMHomeManager, didRemove: HMHome)](./homemanager%28_,didremove%29.md)
  Tells the delegate that the home manager removed a home.
- [func homeManagerDidUpdatePrimaryHome(HMHomeManager)](./homemanagerdidupdateprimaryhome%28_%29.md)
  Tells the delegate that the home manager updated its primary home.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomemanagerdelegate/homemanagerdidupdatehomes(_:))*