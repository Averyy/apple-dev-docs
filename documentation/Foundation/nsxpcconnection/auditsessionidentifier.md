# auditSessionIdentifier

**Framework**: Foundation  
**Kind**: property

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

#### Discussion

This attribute may be used by the listener delegate to accept or reject connections.

## See Also

- [var processIdentifier: pid_t](nsxpcconnection/processidentifier.md)
  The process ID (PID) of the connecting process.
- [var effectiveGroupIdentifier: gid_t](nsxpcconnection/effectivegroupidentifier.md)
  The effective group ID (EGID) of the connecting process.
- [var effectiveUserIdentifier: uid_t](nsxpcconnection/effectiveuseridentifier.md)
  The effective user ID (EUID) of the connecting process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpcconnection/auditsessionidentifier)*