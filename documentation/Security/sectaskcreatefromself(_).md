# SecTaskCreateFromSelf(_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Creates a task object for the current task.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func SecTaskCreateFromSelf(_ allocator: CFAllocator?) -> SecTask?
```

```c
SecTaskRefSecTaskCreateFromSelf(CFAllocatorRef allocator);
```

## Return Value

A new task, or `NULL` on error. In Objective-C, call the [`CFRelease`](../CoreFoundation/cfrelease.md) function to free this task’s memory when you are done with it.

## Parameters

- `allocator`: An allocator. Pass `NULL` to use the default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectaskcreatefromself(_:))*