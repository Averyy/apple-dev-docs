# getGroupMembership(with:completion:)

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
func getGroupMembership(with params: MTRGroupsClusterGetGroupMembershipParams, completion: @escaping @Sendable (MTRGroupsClusterGetGroupMembershipResponseParams?, (any Error)?) -> Void)
```

```swift
func groupMembership(with params: MTRGroupsClusterGetGroupMembershipParams) async throws -> MTRGroupsClusterGetGroupMembershipResponseParams
```

```objc
- (void) getGroupMembershipWithParams:(MTRGroupsClusterGetGroupMembershipParams *) params completion:(void (^)(MTRGroupsClusterGetGroupMembershipResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustergroups/getgroupmembership(with:completion:))*