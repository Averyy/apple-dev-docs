# viewGroup(with:completion:)

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
func viewGroup(with params: MTRGroupsClusterViewGroupParams, completion: @escaping @Sendable (MTRGroupsClusterViewGroupResponseParams?, (any Error)?) -> Void)
```

```swift
func viewGroup(with params: MTRGroupsClusterViewGroupParams) async throws -> MTRGroupsClusterViewGroupResponseParams
```

```objc
- (void) viewGroupWithParams:(MTRGroupsClusterViewGroupParams *) params completion:(void (^)(MTRGroupsClusterViewGroupResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustergroups/viewgroup(with:completion:))*