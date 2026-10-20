# subscribeAttributeSecurityPolicy(with:subscriptionEstablished:reportHandler:)

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
func subscribeAttributeSecurityPolicy(with params: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: @escaping (MTRThreadNetworkDiagnosticsClusterSecurityPolicy?, (any Error)?) -> Void)
```

```objc
- (void) subscribeAttributeSecurityPolicyWithParams:(MTRSubscribeParams *) params subscriptionEstablished:(MTRSubscriptionEstablishedHandler) subscriptionEstablished reportHandler:(void (^)(MTRThreadNetworkDiagnosticsClusterSecurityPolicy *value, NSError *error)) reportHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterthreadnetworkdiagnostics/subscribeattributesecuritypolicy(with:subscriptionestablished:reporthandler:))*