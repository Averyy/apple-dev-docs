# init(networkIdentifier:)

**Framework**: Nearby Interaction  
**Kind**: init  
**Role**: Initializer

Initializes a Downlink Time-Difference-of-Arrival (DL-TDOA) configuration for a specific tracked area.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
init(networkIdentifier: Int)
```

```objc
- (instancetype) initWithNetworkIdentifier:(NSInteger) networkIdentifier;
```

## Discussion

When you call this method, the [`discoveryMethod`](./discoverymethod-swift.property.md) defaults to [`NIDLTDOAConfiguration.DiscoveryMethod.bluetoothLowEnergy`](./discoverymethod-swift.enum/bluetoothlowenergy.md). To initialize a configuration and specify your deployment’s discovery method, call [`init(networkIdentifier:discoveryMethod:)`](./init%28networkidentifier,discoverymethod%29.md) instead.

## Parameters

- `networkIdentifier`: An identifier for the DL-TDOA network that the session belongs to. Anchors that share the same network ID are part of one ranging network that can span multiple anchor clusters.

## See Also

### Creating a configuration
- [init(networkIdentifier: Int, discoveryMethod: NIDLTDOAConfiguration.DiscoveryMethod)](./init%28networkidentifier,discoverymethod%29.md)
  Initializes a DL-TDOA configuration with a network identifier and discovery method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidltdoaconfiguration/init(networkidentifier:))*