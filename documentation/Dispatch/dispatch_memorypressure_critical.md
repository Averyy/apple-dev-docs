# DISPATCH_MEMORYPRESSURE_CRITICAL

**Framework**: Dispatch  
**Kind**: var  
**Role**: Global Variable

The system memory pressure condition is at the critical stage.

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
var DISPATCH_MEMORYPRESSURE_CRITICAL: Int32 { get }
```

```c
#define DISPATCH_MEMORYPRESSURE_CRITICAL
```

## Discussion

Apps should release as much memory as possible.

## See Also

### Memory Pressure Event Flags
- [var DISPATCH_MEMORYPRESSURE_WARN: Int32](./dispatch_memorypressure_warn.md)
  The system memory pressure condition is at the warning stage.
- [var DISPATCH_MEMORYPRESSURE_NORMAL: Int32](./dispatch_memorypressure_normal.md)
  The system memory pressure condition has returned to normal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_memorypressure_critical)*