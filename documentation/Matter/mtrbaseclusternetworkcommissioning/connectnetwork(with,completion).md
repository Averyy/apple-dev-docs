# connectNetwork(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
func connectNetwork(with params: MTRNetworkCommissioningClusterConnectNetworkParams, completion: @escaping @Sendable (MTRNetworkCommissioningClusterConnectNetworkResponseParams?, (any Error)?) -> Void)
```

```swift
func connectNetwork(with params: MTRNetworkCommissioningClusterConnectNetworkParams) async throws -> MTRNetworkCommissioningClusterConnectNetworkResponseParams
```

```objc
- (void) connectNetworkWithParams:(MTRNetworkCommissioningClusterConnectNetworkParams *) params completion:(void (^)(MTRNetworkCommissioningClusterConnectNetworkResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusternetworkcommissioning/connectnetwork(with:completion:))*