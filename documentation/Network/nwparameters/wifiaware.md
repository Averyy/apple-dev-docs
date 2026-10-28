# wifiAware

**Framework**: Network  
**Kind**: property  
**Role**: Instance Property

Get and set Wi-Fi Aware specific connection parameters.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
final var wifiAware: WAParameters { get set }
```

## Discussion

If no Wi-Fi Aware specific properties were previously set, the `WAParameters/defaults` are assumed.

The following code is an example of creating the `NWParameters`, setting, and getting the WiFi Aware parameters.

```swift
// Create NWParameters
var networkParameters = NWParameters()

// Set Wi-Fi Aware Parameters
networkParameters.wifiAware = .defaults

// Get Wi-Fi Aware Parameters
let wifiAwareParameters = networkParameters.wifiAware
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparameters/wifiaware)*