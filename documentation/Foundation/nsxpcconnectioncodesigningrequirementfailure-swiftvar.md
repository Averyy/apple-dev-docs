# NSXPCConnectionCodeSigningRequirementFailure

**Framework**: Foundation  
**Kind**: var

A code-signing requirement check failed.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var NSXPCConnectionCodeSigningRequirementFailure: Int { get }
```

#### Discussion

This error represents a failure to meet the requirement set by a call to [`NSXPCConnection`](nsxpcconnection.md)‘s [`setCodeSigningRequirement(_:)`](nsxpcconnection/setcodesigningrequirement(_:).md) method, or NSXPCConnectionListener’s [`setConnectionCodeSigningRequirement(_:)`](nsxpclistener/setconnectioncodesigningrequirement(_:).md) method.

## See Also

- [var NSXPCConnectionInterrupted: Int](nsxpcconnectioninterrupted-swift.var.md)
  The XPC connection was interrupted.
- [var NSXPCConnectionInvalid: Int](nsxpcconnectioninvalid-swift.var.md)
  The XPC connection was invalid.
- [var NSXPCConnectionReplyInvalid: Int](nsxpcconnectionreplyinvalid-swift.var.md)
  The XPC connection reply was invalid.
- [var NSXPCConnectionErrorMinimum: Int](nsxpcconnectionerrorminimum-swift.var.md)
  The lower bounds of XPC connection error code values.
- [var NSXPCConnectionErrorMaximum: Int](nsxpcconnectionerrormaximum-swift.var.md)
  The upper bounds of XPC connection error code values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpcconnectioncodesigningrequirementfailure-swift.var)*