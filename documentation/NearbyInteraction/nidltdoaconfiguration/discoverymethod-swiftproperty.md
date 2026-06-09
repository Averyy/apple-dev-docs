# discoveryMethod

**Framework**: Nearby Interaction  
**Kind**: property

The technology your app uses to discover DL-TDOA anchors.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
var discoveryMethod: NIDLTDOAConfiguration.DiscoveryMethod { get set }
```

#### Discussion

This property specifies Wi-Fi or Bluetooth Low Energy, depending on how your app scans for nearby DL-TDOA anchors. Set this property when configuring the session by calling [`init(networkIdentifier:discoveryMethod:)`](nidltdoaconfiguration/init(networkidentifier:discoverymethod:).md).

If you use the [`init(networkIdentifier:)`](nidltdoaconfiguration/init(networkidentifier:).md) initializer instead, the framework defaults the property to [`NIDLTDOAConfiguration.DiscoveryMethod.bluetoothLowEnergy`](nidltdoaconfiguration/discoverymethod-swift.enum/bluetoothlowenergy.md).

## See Also

- [NIDLTDOAConfiguration.DiscoveryMethod](nidltdoaconfiguration/discoverymethod-swift.enum.md)
  The technologies an app can use to discover Downlink Time-Difference-of-Arrival anchors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidltdoaconfiguration/discoverymethod-swift.property)*