# expiredDNSBehavior(_:)

**Framework**: Network  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Allow or prohibit the use of expired DNS answers during connection establishment.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func expiredDNSBehavior(_ behavior: NWParameters.ExpiredDNSBehavior) -> Self
```

## Discussion

If allowed, a DNS answer that was previously returned may be re-used for new connections even after the answers are considered expired. A query for fresh answers will be sent in parallel, and the fresh answers will be used as alternate addresses in case the expired answers do not result in successful connections.

By default, this value is `.systemDefault`, which allows the system to determine if it is appropriate to use expired answers.

## Parameters

- `behavior`: The expired DNS behavior to use.

## Default Implementations

### NWParametersProvider Implementations
- [func expiredDNSBehavior(NWParameters.ExpiredDNSBehavior) -> Self](./expireddnsbehavior%28_%29-3w6lp.md)
  Allow or prohibit the use of expired DNS answers during connection establishment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparametersprovider/expireddnsbehavior(_:))*