# authorization

**Framework**: Core Bluetooth  
**Kind**: property  
**Role**: Type Property

The current authorization status for using Bluetooth.

**Availability**:
- iOS 13.1+
- iPadOS 13.1+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class var authorization: CBManagerAuthorization { get }
```

```objc
@property (class, nonatomic, assign, readonly) CBManagerAuthorization authorization;
```

#### Discussion

Check this property in your implementation of the delegate methods [`centralManagerDidUpdateState(_:)`](../cbcentralmanagerdelegate/centralmanagerdidupdatestate%28_%29.md) and [`peripheralManagerDidUpdateState(_:)`](../cbperipheralmanagerdelegate/peripheralmanagerdidupdatestate%28_%29.md) to determine whether your app can use Core Bluetooth. You can also use it to check the app’s authorization status before creating a [`CBManager`](../cbmanager.md) instance.

The initial value of this property is [`CBManagerAuthorization.notDetermined`](../cbmanagerauthorization/notdetermined.md).

## See Also

### Determining Authorization State
- [enum CBManagerAuthorization](../cbmanagerauthorization.md)
  The current authorization state of a Core Bluetooth manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbmanager/authorization-swift.type.property)*