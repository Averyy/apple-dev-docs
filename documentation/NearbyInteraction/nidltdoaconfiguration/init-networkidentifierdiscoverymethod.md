# init(networkIdentifier:discoveryMethod:)

**Framework**: Nearby Interaction  
**Kind**: init

Initializes a DL-TDOA configuration with a network identifier and discovery method.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
init(networkIdentifier: Int, discoveryMethod: NIDLTDOAConfiguration.DiscoveryMethod)
```

#### Discussion

Use this initializer to create a DL-TDOA configuration that specifies a network identifier for a specific tracked area and the method it uses to discover anchors in the tracked area. The network identifier corresponds to the session ID configured in the DL-TDOA anchors. Anchors with the same session ID belong to the same tracked area.

Specify the method your app uses to discover anchors among [`NIDLTDOAConfiguration.DiscoveryMethod.wifi`](nidltdoaconfiguration/discoverymethod-swift.enum/wifi.md) and [`NIDLTDOAConfiguration.DiscoveryMethod.bluetoothLowEnergy`](nidltdoaconfiguration/discoverymethod-swift.enum/bluetoothlowenergy.md) to match the infrastructure in your deployment environment.

```swift
let configuration = NIDLTDOAConfiguration(
    networkIdentifier: 1,
    discoveryMethod: .wifi
)
session.run(configuration)
```

## Parameters

- `networkIdentifier`: An ID that distinguishes among multiple tracked areas if there’s more than one tracked area in the vicinity.
- `discoveryMethod`: The technology that the session uses to discover DL-TDOA anchors.

## See Also

- [init(networkIdentifier: Int)](nidltdoaconfiguration/init(networkidentifier:).md)
  Initializes a Downlink Time-Difference-of-Arrival (DL-TDOA) configuration for a specific tracked area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidltdoaconfiguration/init(networkidentifier:discoverymethod:))*