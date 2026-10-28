# auditSessionIdentifier

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The BSM audit session identifier for the connecting process.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var auditSessionIdentifier: au_asid_t { get }
```

```objc
@property (readonly) au_asid_t auditSessionIdentifier;
```

## Discussion

This attribute may be used by the listener delegate to accept or reject connections.

## See Also

### Working with security attributes
- [var processIdentifier: pid_t](./processidentifier.md)
  The process ID (PID) of the connecting process.
- [var effectiveGroupIdentifier: gid_t](./effectivegroupidentifier.md)
  The effective group ID (EGID) of the connecting process.
- [var effectiveUserIdentifier: uid_t](./effectiveuseridentifier.md)
  The effective user ID (EUID) of the connecting process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpcconnection/auditsessionidentifier)*