# id(_:)

**Framework**: PermissionKit  
**Kind**: method

Binds a view’s identity to the given proxy value.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 26.0+ (Beta)
- watchOS 6.0+

## Declaration

```swift
nonisolated
func id<ID>(_ id: ID) -> some View where ID : Hashable
```

#### Discussion

When the proxy value specified by the `id` parameter changes, the identity of the view — for example, its state — is reset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton/id(_:))*