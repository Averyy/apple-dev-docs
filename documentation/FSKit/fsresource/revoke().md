# revoke()

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method

Revokes the resource.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func revoke()
```

```objc
- (void) revoke;
```

## Discussion

This method works by stripping away any underlying privileges associated with the resource. This effectively disconnects this object from its underlying resource.

## See Also

### Revoking the resource
- [var isRevoked: Bool](./isrevoked.md)
  A Boolean value that indicates whether the resource is revoked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsresource/revoke())*