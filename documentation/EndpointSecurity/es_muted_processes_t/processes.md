# processes

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

An array containing the muted processes.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var processes: UnsafePointer<es_muted_process_t>!
```

```c
const es_muted_process_t * processes;
```

## See Also

### Accessing Muted Processes
- [struct es_muted_process_t](../es_muted_process_t.md)
  A structure that describes a process’s muted events.
- [var count: Int](./count.md)
  The number of elements in the processes array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_muted_processes_t/processes)*