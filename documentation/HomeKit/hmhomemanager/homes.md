# homes

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

An array of all homes managed by this home manager.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var homes: [HMHome] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<HMHome *> * homes;
```

## Discussion

When you create a new home manager, its [`homes`](./homes.md) array is empty by default. You can only be sure that this array is properly initialized with data from the shared HomeKit database after the manager calls its delegate’s [`homeManagerDidUpdateHomes(_:)`](../hmhomemanagerdelegate/homemanagerdidupdatehomes%28_%29.md) method for the first time.

## See Also

### Working with the home layout
- [class HMHome](../hmhome.md)
  The primary unit of living space, typically composed of rooms organized into zones.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomemanager/homes)*