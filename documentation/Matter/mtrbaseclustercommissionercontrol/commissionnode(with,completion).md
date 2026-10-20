# commissionNode(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command CommissionNode

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
func commissionNode(with params: MTRCommissionerControlClusterCommissionNodeParams, completion: @escaping @Sendable (MTRCommissionerControlClusterReverseOpenCommissioningWindowParams?, (any Error)?) -> Void)
```

```swift
func commissionNode(with params: MTRCommissionerControlClusterCommissionNodeParams) async throws -> MTRCommissionerControlClusterReverseOpenCommissioningWindowParams
```

```objc
- (void) commissionNodeWithParams:(MTRCommissionerControlClusterCommissionNodeParams *) params completion:(void (^)(MTRCommissionerControlClusterReverseOpenCommissioningWindowParams *data, NSError *error)) completion;
```

#### Discussion

This command is sent by a client to request that the server begins commissioning a previously approved request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustercommissionercontrol/commissionnode(with:completion:))*