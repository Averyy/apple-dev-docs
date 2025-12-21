# NWParameters.ServiceClass.signaling

**Framework**: Network  
**Kind**: case

A service type for low-loss tolerant, inelastic flow, jitter tolerant, bursty but short rate, and variable size connections.

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
case signaling
```

#### Discussion

An example of traffic that uses this service type occurs when the system needs to establish and tear down a VoIP call.

## See Also

- [NWParameters.ServiceClass.bestEffort](nwparameters/serviceclass-swift.enum/besteffort.md)
  The default service type.
- [NWParameters.ServiceClass.background](nwparameters/serviceclass-swift.enum/background.md)
  A service type for high-delay tolerant, high-loss tolerant, elastic flow, and variable size connections.
- [NWParameters.ServiceClass.interactiveVideo](nwparameters/serviceclass-swift.enum/interactivevideo.md)
  A service type for low-delay tolerant, very low-loss tolerant, inelastic flow, and constant packet rate connections.
- [NWParameters.ServiceClass.interactiveVoice](nwparameters/serviceclass-swift.enum/interactivevoice.md)
  A service type for low-delay tolerant, very low-loss tolerant, inelastic flow, and constant packet rate connections.
- [NWParameters.ServiceClass.responsiveData](nwparameters/serviceclass-swift.enum/responsivedata.md)
  A service type for medium-delay tolerant, inelastic flow, and bursty connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparameters/serviceclass-swift.enum/signaling)*