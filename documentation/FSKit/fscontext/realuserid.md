# realUserID

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

The caller’s real user ID.

**Availability**:
- macOS 27.0+

## Declaration

```swift
var realUserID: Int { get }
```

```objc
@property (readonly) NSInteger realUserID;
```

## See Also

### Accessing context properties
- [var effectiveUserID: Int](./effectiveuserid.md)
  The caller’s effective user ID.
- [var realGroupID: Int](./realgroupid.md)
  The caller’s real group ID.
- [var effectiveGroupID: Int](./effectivegroupid.md)
  The caller’s effective group ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscontext/realuserid)*