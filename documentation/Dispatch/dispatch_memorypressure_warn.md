# DISPATCH_MEMORYPRESSURE_WARN

**Framework**: Dispatch  
**Kind**: var  
**Role**: Global Variable

The system memory pressure condition is at the warning stage.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var DISPATCH_MEMORYPRESSURE_WARN: Int32 { get }
```

```c
#define DISPATCH_MEMORYPRESSURE_WARN
```

#### Discussion

Apps should release memory that they do not need right now.

## See Also

### Memory Pressure Event Flags
- [var DISPATCH_MEMORYPRESSURE_NORMAL: Int32](./dispatch_memorypressure_normal.md)
  The system memory pressure condition has returned to normal.
- [var DISPATCH_MEMORYPRESSURE_CRITICAL: Int32](./dispatch_memorypressure_critical.md)
  The system memory pressure condition is at the critical stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_memorypressure_warn)*