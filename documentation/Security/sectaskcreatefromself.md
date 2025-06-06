# SecTaskCreateFromSelf(_:)

**Framework**: Security  
**Kind**: func

Creates a task object for the current task.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func SecTaskCreateFromSelf(_ allocator: CFAllocator?) -> SecTask?
```

#### Return Value

A new task, or `NULL` on error. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) function to free this task’s memory when you are done with it.

## Parameters

- `allocator`: An allocator. Pass   to use the default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectaskcreatefromself(_:))*