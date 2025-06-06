# remoteObjectProxy()

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

Returns a proxy object with no error handling block.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func remoteObjectProxy() -> Any
```

#### Discussion

Messages sent to the proxy object are sent over the wire to the other side of the connection. All messages must be ‘void’ return type. Control may be returned to the caller before the message is sent. The resulting proxy object conforms to the `NSXPCProxyCreating` protocol.

## See Also

- [Daemons and Services Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/Introduction.html#//apple_ref/doc/uid/10000172i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpcproxycreating/remoteobjectproxy())*