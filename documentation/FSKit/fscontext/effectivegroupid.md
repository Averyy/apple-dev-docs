# effectiveGroupID

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

The caller’s effective group ID.

**Availability**:
- macOS 27.0+

## Declaration

```swift
var effectiveGroupID: Int { get }
```

```objc
@property (readonly) NSInteger effectiveGroupID;
```

## See Also

### Accessing context properties
- [var realUserID: Int](./realuserid.md)
  The caller’s real user ID.
- [var effectiveUserID: Int](./effectiveuserid.md)
  The caller’s effective user ID.
- [var realGroupID: Int](./realgroupid.md)
  The caller’s real group ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscontext/effectivegroupid)*