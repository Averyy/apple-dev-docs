# isRevoked

**Framework**: FSKit  
**Kind**: property

A Boolean value that indicates whether the resource is revoked.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var isRevoked: Bool { get }
```

#### Discussion

If this is a proxy resource, the value of this property is always `true` (Swift) or `YES` (Objective-C).

## See Also

- [func revoke()](fsresource/revoke.md)
  Revokes the resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsresource/isrevoked)*