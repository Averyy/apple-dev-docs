# NSXPCConnectionErrorMinimum

**Framework**: Foundation  
**Kind**: case  
**Role**: Enumeration Case

The lower bounds of XPC connection error code values.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
NSXPCConnectionErrorMinimum
```

## Discussion

All XPC error codes have values between [`NSXPCConnectionErrorMinimum`](./nsxpcconnectionerrorminimum-swift.var.md) and [`NSXPCConnectionErrorMaximum`](./nsxpcconnectionerrormaximum-swift.var.md), exclusive. This constant does not correspond to any particular error.

## See Also

### Error codes
- [NSXPCConnectionInterrupted](./nsxpcconnectioninterrupted-c.enum.case.md)
  The XPC connection was interrupted.
- [NSXPCConnectionInvalid](./nsxpcconnectioninvalid-c.enum.case.md)
  The XPC connection was invalid.
- [NSXPCConnectionReplyInvalid](./nsxpcconnectionreplyinvalid-c.enum.case.md)
  The XPC connection reply was invalid.
- [NSXPCConnectionErrorMaximum](./nsxpcconnectionerrormaximum-c.enum.case.md)
  The upper bounds of XPC connection error code values.
- [NSXPCConnectionCodeSigningRequirementFailure](./nsxpcconnectioncodesigningrequirementfailure-c.enum.case.md)
  A code-signing requirement check failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpcconnectionerrorminimum-c.enum.case)*