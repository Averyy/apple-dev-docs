# changeToMode(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command ChangeToMode

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
func changeToMode(with params: MTRDishwasherModeClusterChangeToModeParams, completion: @escaping @Sendable (MTRDishwasherModeClusterChangeToModeResponseParams?, (any Error)?) -> Void)
```

```swift
func changeToMode(with params: MTRDishwasherModeClusterChangeToModeParams) async throws -> MTRDishwasherModeClusterChangeToModeResponseParams
```

```objc
- (void) changeToModeWithParams:(MTRDishwasherModeClusterChangeToModeParams *) params completion:(void (^)(MTRDishwasherModeClusterChangeToModeResponseParams *data, NSError *error)) completion;
```

## Discussion

This command is used to change device modes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterdishwashermode/changetomode(with:completion:))*