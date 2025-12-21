# listener(_:shouldAcceptNewConnection:)

**Framework**: Foundation  
**Kind**: method

Accepts or rejects a new connection to the listener.

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
optional func listener(_ listener: NSXPCListener, shouldAcceptNewConnection newConnection: NSXPCConnection) -> Bool
```

#### Discussion

To accept the connection, first configure the connection if desired, then call [`resume()`](nsxpcconnection/resume().md) on the new connection, then return [`true`](https://developer.apple.com/documentation/Swift/true).

To reject the connect, return a value of [`false`](https://developer.apple.com/documentation/Swift/false). This causes the connection object to be invalidated.

In this method, you can also set up properties on the connection object, such as its exported object and interfaces. Be sure to call [`resume()`](nsxpcconnection/resume().md) when you are finished configuring the connection object and are ready for it to receive messages.

## See Also

- [Daemons and Services Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/Introduction.html#//apple_ref/doc/uid/10000172i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpclistenerdelegate/listener(_:shouldacceptnewconnection:))*