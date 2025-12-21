# wifiAware(_:)

**Framework**: Network  
**Kind**: method

Configure Wi-Fi Aware properties on an `NWParameters` object.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
final func wifiAware(_ configurator: (inout WAParameters) -> Void) -> Self
```

#### Return Value

The updated parameters, with the configured Wi-Fi Aware parameters applied.

#### Discussion

If not previously set, parameters will have `WAParameters/defaults` applied initially.

Example:

```swift
// Create NWParameters & apply wifiAware parameters
let networkParameters = NWParameters().wifiAware {
	$0 = .defaults
}
```

## Parameters

- `configurator`: The function that will apply the desired   to the network parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparameters/wifiaware(_:))*