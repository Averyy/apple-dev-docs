# setDSTOffsetWith(_:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command SetDSTOffset

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
func setDSTOffsetWith(_ params: MTRTimeSynchronizationClusterSetDSTOffsetParams, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func setDSTOffsetWith(_ params: MTRTimeSynchronizationClusterSetDSTOffsetParams) async throws
```

```objc
- (void) setDSTOffsetWithParams:(MTRTimeSynchronizationClusterSetDSTOffsetParams *) params completion:(MTRStatusCompletion) completion;
```

#### Discussion

This command is used to set the DST offsets for a node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustertimesynchronization/setdstoffsetwith(_:completion:))*