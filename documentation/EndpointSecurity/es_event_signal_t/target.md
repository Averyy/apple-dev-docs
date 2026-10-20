# target

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The process that the signal targets.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var target: UnsafeMutablePointer<es_process_t>
```

```c
es_process_t * target;
```

## See Also

### Inspecting Event Properties
- [var sig: Int32](./sig.md)
  The signal number sent to the target process.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](./reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_signal_t/target)*