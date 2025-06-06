# anonymous()

**Framework**: Foundation  
**Kind**: method

Returns a new anonymous listener connection.

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
class func anonymous() -> NSXPCListener
```

#### Discussion

Other processes can connect to this listener by passing this listener object’s `NSXPCListenerEndpoint` to the [`init(listenerEndpoint:)`](nsxpcconnection/init(listenerendpoint:).md) method of an [`NSXPCConnection`](nsxpcconnection.md) object.

## See Also

- [class func service() -> NSXPCListener](nsxpclistener/service.md)
  Returns the singleton listener used to listen for incoming connections in an XPC service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpclistener/anonymous())*