# addGroup(with:completion:)

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
func addGroup(with params: MTRGroupsClusterAddGroupParams, completion: @escaping @Sendable (MTRGroupsClusterAddGroupResponseParams?, (any Error)?) -> Void)
```

```swift
func addGroup(with params: MTRGroupsClusterAddGroupParams) async throws -> MTRGroupsClusterAddGroupResponseParams
```

```objc
- (void) addGroupWithParams:(MTRGroupsClusterAddGroupParams *) params completion:(void (^)(MTRGroupsClusterAddGroupResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustergroups/addgroup(with:completion:))*