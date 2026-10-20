# pid

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Instance Property

The process identifier of the client.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var pid: pid_t { get }
```

```objc
@property (atomic, readonly) pid_t pid;
```

## See Also

### Identifying a Client
- [var clientID: UUID](./clientid.md)
  A unique client identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionclient/pid)*