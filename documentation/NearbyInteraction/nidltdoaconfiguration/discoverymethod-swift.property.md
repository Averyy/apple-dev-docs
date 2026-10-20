# discoveryMethod

**Framework**: Nearby Interaction  
**Kind**: property  
**Role**: Instance Property

The technology your app uses to discover DL-TDOA anchors.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
var discoveryMethod: NIDLTDOAConfiguration.DiscoveryMethod { get set }
```

```objc
@property (nonatomic, assign) NIDLTDOADiscoveryMethod discoveryMethod;
```

#### Discussion

This property specifies Wi-Fi or Bluetooth Low Energy, depending on how your app scans for nearby DL-TDOA anchors. Set this property when configuring the session by calling [`init(networkIdentifier:discoveryMethod:)`](./init%28networkidentifier,discoverymethod%29.md).

If you use the [`init(networkIdentifier:)`](./init%28networkidentifier%29.md) initializer instead, the framework defaults the property to [`NIDLTDOAConfiguration.DiscoveryMethod.bluetoothLowEnergy`](./discoverymethod-swift.enum/bluetoothlowenergy.md).

## See Also

### Specifing the discovery method
- [NIDLTDOAConfiguration.DiscoveryMethod](./discoverymethod-swift.enum.md)
  The technologies an app can use to discover Downlink Time-Difference-of-Arrival anchors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidltdoaconfiguration/discoverymethod-swift.property)*