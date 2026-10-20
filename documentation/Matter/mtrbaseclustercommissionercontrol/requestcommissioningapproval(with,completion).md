# requestCommissioningApproval(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command RequestCommissioningApproval

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
func requestCommissioningApproval(with params: MTRCommissionerControlClusterRequestCommissioningApprovalParams, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func requestCommissioningApproval(with params: MTRCommissionerControlClusterRequestCommissioningApprovalParams) async throws
```

```objc
- (void) requestCommissioningApprovalWithParams:(MTRCommissionerControlClusterRequestCommissioningApprovalParams *) params completion:(MTRStatusCompletion) completion;
```

#### Discussion

This command is sent by a client to request approval for a future CommissionNode call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustercommissionercontrol/requestcommissioningapproval(with:completion:))*