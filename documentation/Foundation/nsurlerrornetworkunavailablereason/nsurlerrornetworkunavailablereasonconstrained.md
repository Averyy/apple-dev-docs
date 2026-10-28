# NSURLErrorNetworkUnavailableReasonConstrained

**Framework**: Foundation  
**Kind**: case  
**Role**: Enumeration Case

A reason that indicates network is unavailable because the user enabled “Low Data Mode” in the Settings app.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```c
NSURLErrorNetworkUnavailableReasonConstrained
```

## Discussion

This reason occurs when the following conditions are true:

- The only available network is cellular.
- The user has enabled “Low Data Mode” option in the Cellular Data Options section of the Settings app.
- The [`URLSessionConfiguration`](../urlsessionconfiguration.md) property [`allowsConstrainedNetworkAccess`](../urlsessionconfiguration/allowsconstrainednetworkaccess.md) is [`false`](../../Swift/false.md).

## See Also

### Unavailability reasons
- [NSURLErrorNetworkUnavailableReasonCellular](./nsurlerrornetworkunavailablereasoncellular.md)
  A reason that indicates network is unavailable because the interface is cellular and cellular network is disabled.
- [NSURLErrorNetworkUnavailableReasonExpensive](./nsurlerrornetworkunavailablereasonexpensive.md)
  A reason that indicates network is unavailable because the system marked the interface as expensive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlerrornetworkunavailablereason/nsurlerrornetworkunavailablereasonconstrained)*