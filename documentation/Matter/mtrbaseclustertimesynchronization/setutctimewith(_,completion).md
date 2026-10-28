# setUTCTimeWith(_:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command SetUTCTime

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
func setUTCTimeWith(_ params: MTRTimeSynchronizationClusterSetUTCTimeParams, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func setUTCTimeWith(_ params: MTRTimeSynchronizationClusterSetUTCTimeParams) async throws
```

```objc
- (void) setUTCTimeWithParams:(MTRTimeSynchronizationClusterSetUTCTimeParams *) params completion:(MTRStatusCompletion) completion;
```

## Discussion

This command is used to set the UTC time of the node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustertimesynchronization/setutctimewith(_:completion:))*