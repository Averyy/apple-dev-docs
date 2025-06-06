# setCodeSigningRequirement(_:)

**Framework**: Foundation  
**Kind**: method

Sets the code signing requirement for this connection.

**Availability**:
- macOS 13.0+

## Declaration

```swift
func setCodeSigningRequirement(_ requirement: String)
```

#### Discussion

Use this method to enforce a code-signing requirement on the peer process of an XPC connection.

The following example shows how a client can ensure that the XPC service on the other end of a connection has a specific entitlement.

Calling this method with a malformed `requirement` results in a fatal error in Swift, or throws an exception in Objective-C. If new messages don’t match the requirement, the connection becomes invalidated.

Call this method before calling [`resume()`](nsxpcconnection/resume().md), since it’s an XPC error to call this method more than once.

## Parameters

- `requirement`: A string that describes requirements expected of the connection peer. See   for more information on the code signing format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpcconnection/setcodesigningrequirement(_:))*