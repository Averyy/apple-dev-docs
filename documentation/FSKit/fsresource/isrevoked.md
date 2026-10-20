# isRevoked

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the resource is revoked.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var isRevoked: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isRevoked) BOOL revoked;
```

#### Discussion

If this is a proxy resource, the value of this property is always `true` (Swift) or `YES` (Objective-C).

## See Also

### Revoking the resource
- [func revoke()](./revoke%28%29.md)
  Revokes the resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsresource/isrevoked)*