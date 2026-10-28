# wifiAware(_:)

**Framework**: Network  
**Kind**: method  
**Role**: Instance Method

Configure Wi-Fi Aware properties on an `NetworkConnection`

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
func wifiAware(_ configurator: (inout WAParameters) -> Void) -> NWParametersBuilder<Top, repeat each P>
```

Available when `Top` conforms to `NetworkProtocolOptions` and `each P` conforms to `NetworkProtocolOptions`.

## Return Value

The updated parameters, with the configured Wi-Fi Aware parameters applied.

## Discussion

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

- `configurator`: The function that will apply the desired `WAParameters` to the network parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparametersbuilder/wifiaware(_:))*