# NWParameters.ServiceClass.background

**Framework**: Network  
**Kind**: case  
**Role**: Case

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

Use this service type when, for example, you’re managing traffic that prefetches content and makes it available when the person chooses to view it.

## See Also

### Service Classes
- [NWParameters.ServiceClass.bestEffort](./besteffort.md)
  The default service type.
- [NWParameters.ServiceClass.interactiveVideo](./interactivevideo.md)
  A service type for low-delay tolerant, very low-loss tolerant, inelastic flow, and constant packet rate connections.
- [NWParameters.ServiceClass.interactiveVoice](./interactivevoice.md)
  A service type for low-delay tolerant, very low-loss tolerant, inelastic flow, and constant packet rate connections.
- [NWParameters.ServiceClass.responsiveData](./responsivedata.md)
  A service type for medium-delay tolerant, inelastic flow, and bursty connections.
- [NWParameters.ServiceClass.signaling](./signaling.md)
  A service type for low-loss tolerant, inelastic flow, jitter tolerant, bursty but short rate, and variable size connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparameters/serviceclass-swift.enum/background)*