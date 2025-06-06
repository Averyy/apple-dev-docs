# sessionKeepCurrentBootstrap

**Framework**: Security  
**Kind**: property

The caller has allocated sub-bootstrap.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
static var sessionKeepCurrentBootstrap: SessionCreationFlags { get }
```

#### Discussion

If you create a subset port on your own, you can force

the [`SessionCreate(_:_:)`](sessioncreate(_:_:).md) function to use it by passing this flag in the `flags` parameter. However, you can’t supersede a prior call that way; only a single [`SessionCreate(_:_:)`](sessioncreate(_:_:).md) call is allowed for each session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sessioncreationflags/sessionkeepcurrentbootstrap)*