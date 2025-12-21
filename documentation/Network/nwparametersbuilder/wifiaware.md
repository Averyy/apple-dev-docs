# wifiAware(_:)

**Framework**: Network  
**Kind**: method

Configure Wi-Fi Aware properties on an `NetworkConnection`

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
func wifiAware(_ configurator: (inout WAParameters) -> Void) -> NWParametersBuilder<Top, repeat each P>
```

#### Return Value

The updated parameters, with the configured Wi-Fi Aware parameters applied.

#### Discussion

If not previously set, parameters will have `WAParameters/defaults` applied initially.

Example:

```swift
let connection = NetworkConnection(to: endpoint, using: .parameters {
	UDP()
}.wifiAware {
	$0 = .defaults
}
```

## Parameters

- `configurator`: The function that will apply the desired   to the network parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparametersbuilder/wifiaware(_:))*