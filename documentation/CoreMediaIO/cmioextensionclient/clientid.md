# clientID

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Instance Property

A unique client identifier.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var clientID: UUID { get }
```

```objc
@property (atomic, copy, readonly) NSUUID * clientID;
```

## See Also

### Identifying a Client
- [var pid: pid_t](./pid.md)
  The process identifier of the client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionclient/clientid)*