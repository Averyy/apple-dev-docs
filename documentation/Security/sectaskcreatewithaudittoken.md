# SecTaskCreateWithAuditToken(_:_:)

**Framework**: Security  
**Kind**: func

Creates a task object for the task that sent the Mach message represented by the audit token.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func SecTaskCreateWithAuditToken(_ allocator: CFAllocator?, _ token: audit_token_t) -> SecTask?
```

#### Return Value

A new task, or `NULL` on error. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) function to free this task’s memory when you are done with it.

## Parameters

- `allocator`: An allocator. Pass   to use the default.
- `token`: The audit token of a Mach message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectaskcreatewithaudittoken(_:_:))*