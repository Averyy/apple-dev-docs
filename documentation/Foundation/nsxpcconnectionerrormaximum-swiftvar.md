# NSXPCConnectionErrorMaximum

**Framework**: Foundation  
**Kind**: var

The upper bounds of XPC connection error code values.

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
var NSXPCConnectionErrorMaximum: Int { get }
```

#### Discussion

All XPC error codes have values between [`NSXPCConnectionErrorMinimum`](nsxpcconnectionerrorminimum-swift.var.md) and [`NSXPCConnectionErrorMaximum`](nsxpcconnectionerrormaximum-swift.var.md), exclusive. This constant does not correspond to any particular error.

## See Also

- [var NSXPCConnectionInterrupted: Int](nsxpcconnectioninterrupted-swift.var.md)
  The XPC connection was interrupted.
- [var NSXPCConnectionInvalid: Int](nsxpcconnectioninvalid-swift.var.md)
  The XPC connection was invalid.
- [var NSXPCConnectionReplyInvalid: Int](nsxpcconnectionreplyinvalid-swift.var.md)
  The XPC connection reply was invalid.
- [var NSXPCConnectionErrorMinimum: Int](nsxpcconnectionerrorminimum-swift.var.md)
  The lower bounds of XPC connection error code values.
- [var NSXPCConnectionCodeSigningRequirementFailure: Int](nsxpcconnectioncodesigningrequirementfailure-swift.var.md)
  A code-signing requirement check failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpcconnectionerrormaximum-swift.var)*