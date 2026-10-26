# headUnit

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The Bluetooth and iAP2 identifiers of the electric vehicle’s physical head unit.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@NSCopying
var headUnit: INCar.HeadUnit? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INCarHeadUnit * headUnit;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INCarHeadUnit * headUnit;
```

#### Discussion

The system receives the physical head unit’s Bluetooth identifier when the user’s iPhone connects to the vehicle through CarPlay. The system can then find the corresponding vehicle in the user’s Virtual Garage by matching the value it receives against the `bluetoothIdentifier` property of this object.

## See Also

### Getting the Car’s Head Unit
- [INCar.HeadUnit](./headunit-swift.class.md)
  An object that contains the Bluetooth and iAP2 identifiers of the vehicle’s physical head unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incar/headunit-swift.property)*