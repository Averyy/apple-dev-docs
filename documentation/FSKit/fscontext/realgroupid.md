# realGroupID

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

The caller’s real group ID.

**Availability**:
- macOS 27.0+

## Declaration

```swift
var realGroupID: Int { get }
```

```objc
@property (readonly) NSInteger realGroupID;
```

## See Also

### Accessing context properties
- [var realUserID: Int](./realuserid.md)
  The caller’s real user ID.
- [var effectiveUserID: Int](./effectiveuserid.md)
  The caller’s effective user ID.
- [var effectiveGroupID: Int](./effectivegroupid.md)
  The caller’s effective group ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscontext/realgroupid)*