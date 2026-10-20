# stepWithOnOff(with:completion:)

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
func stepWithOnOff(with params: MTRLevelControlClusterStepWithOnOffParams, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func stepWithOnOff(with params: MTRLevelControlClusterStepWithOnOffParams) async throws
```

```objc
- (void) stepWithOnOffWithParams:(MTRLevelControlClusterStepWithOnOffParams *) params completion:(MTRStatusCompletion) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterlevelcontrol/stepwithonoff(with:completion:))*