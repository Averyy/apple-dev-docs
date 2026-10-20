# sig

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The signal number sent to the target process.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var sig: Int32
```

```c
int sig;
```

## See Also

### Inspecting Event Properties
- [var target: UnsafeMutablePointer<es_process_t>](./target.md)
  The process that the signal targets.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](./reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_signal_t/sig)*