# revoke()

**Framework**: FSKit  
**Kind**: method

Revokes the resource.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func revoke()
```

#### Discussion

This method works by stripping away any underlying privileges associated with the resource. This effectively disconnects this object from its underlying resource.

## See Also

- [var isRevoked: Bool](fsresource/isrevoked.md)
  A Boolean value that indicates whether the resource is revoked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsresource/revoke())*