# NWParameters.ServiceClass.background

**Framework**: Network  
**Kind**: case

A service type for high-delay tolerant, high-loss tolerant, elastic flow, and variable size connections.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
case background
```

#### Discussion

An example of this service type is prefetching content so that it’s available when the user chooses to view it.

## See Also

- [NWParameters.ServiceClass.bestEffort](nwparameters/serviceclass-swift.enum/besteffort.md)
  A service type to enable Cellular Network Slicing when not setting the other service types.
- [NWParameters.ServiceClass.interactiveVideo](nwparameters/serviceclass-swift.enum/interactivevideo.md)
  A service type for low-delay tolerant, very low-loss tolerant, inelastic flow, and constant packet rate connections.
- [NWParameters.ServiceClass.interactiveVoice](nwparameters/serviceclass-swift.enum/interactivevoice.md)
  A service type for low-delay tolerant, very low-loss tolerant, inelastic flow, and constant packet rate connections.
- [NWParameters.ServiceClass.responsiveData](nwparameters/serviceclass-swift.enum/responsivedata.md)
  A service type for medium-delay tolerant, elastic and inelastic flow, bursty, and long-lived connections.
- [NWParameters.ServiceClass.signaling](nwparameters/serviceclass-swift.enum/signaling.md)
  A service for low-loss tolerant, inelastic flow, jitter tolerant, bursty but short rate, and variable size connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparameters/serviceclass-swift.enum/background)*