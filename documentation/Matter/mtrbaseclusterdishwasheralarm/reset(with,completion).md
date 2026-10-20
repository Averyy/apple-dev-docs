# reset(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command Reset

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
func reset(with params: MTRDishwasherAlarmClusterResetParams, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func reset(with params: MTRDishwasherAlarmClusterResetParams) async throws
```

```objc
- (void) resetWithParams:(MTRDishwasherAlarmClusterResetParams *) params completion:(MTRStatusCompletion) completion;
```

#### Discussion

This command resets active and latched alarms (if possible).


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterdishwasheralarm/reset(with:completion:))*