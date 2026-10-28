# SecTaskCreateWithAuditToken(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Creates a task object for the task that sent the Mach message represented by the audit token.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func SecTaskCreateWithAuditToken(_ allocator: CFAllocator?, _ token: audit_token_t) -> SecTask?
```

```c
SecTaskRefSecTaskCreateWithAuditToken(CFAllocatorRef allocator, audit_token_t token);
```

## Return Value

A new task, or `NULL` on error. In Objective-C, call the [`CFRelease`](../CoreFoundation/cfrelease.md) function to free this task’s memory when you are done with it.

## Parameters

- `allocator`: An allocator. Pass `NULL` to use the default.
- `token`: The audit token of a Mach message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectaskcreatewithaudittoken(_:_:))*