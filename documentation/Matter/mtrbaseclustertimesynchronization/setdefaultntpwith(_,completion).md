# setDefaultNTPWith(_:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command SetDefaultNTP

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
func setDefaultNTPWith(_ params: MTRTimeSynchronizationClusterSetDefaultNTPParams, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func setDefaultNTPWith(_ params: MTRTimeSynchronizationClusterSetDefaultNTPParams) async throws
```

```objc
- (void) setDefaultNTPWithParams:(MTRTimeSynchronizationClusterSetDefaultNTPParams *) params completion:(MTRStatusCompletion) completion;
```

#### Discussion

This command is used to set the DefaultNTP attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustertimesynchronization/setdefaultntpwith(_:completion:))*