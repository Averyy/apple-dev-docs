# setConnectionCodeSigningRequirement(_:)

**Framework**: Foundation  
**Kind**: method

Sets the code signing requirement for connections to this listener.

**Availability**:
- macOS 13.0+

## Declaration

```swift
func setConnectionCodeSigningRequirement(_ requirement: String)
```

#### Discussion

Use this method to enforce a code-signing requirement on incoming XPC connections.

The following example shows how a listener can ensure that the XPC client service on the other end of a connection has a specific entitlement.

## Parameters

- `requirement`: A string that describes requirements expected of the connection peer. See   for more information on the code signing format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpclistener/setconnectioncodesigningrequirement(_:))*