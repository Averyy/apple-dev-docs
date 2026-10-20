# process

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The process that performed the action defined in a message.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var process: UnsafeMutablePointer<es_process_t>
```

```c
es_process_t * process;
```

## See Also

### Identifying the Source Process
- [struct es_process_t](../es_process_t.md)
  A type that describes a process, as delivered by an Endpoint Security message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_message_t/process)*