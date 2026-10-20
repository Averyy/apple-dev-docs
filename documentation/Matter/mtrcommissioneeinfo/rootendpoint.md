# rootEndpoint

**Framework**: Matter  
**Kind**: property  
**Role**: Instance Property

Endpoint information for the root endpoint of the commissionee. Will be present only if readEndpointInformation is set to YES on MTRCommissioningParameters.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
@NSCopying
var rootEndpoint: MTREndpointInfo? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) MTREndpointInfo * rootEndpoint;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcommissioneeinfo/rootendpoint)*