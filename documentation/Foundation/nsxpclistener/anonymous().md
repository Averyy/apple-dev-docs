# anonymous()

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (NSXPCListener *) anonymousListener;
```

## Discussion

Other processes can connect to this listener by passing this listener object’s `NSXPCListenerEndpoint` to the [`init(listenerEndpoint:)`](../nsxpcconnection/init%28listenerendpoint%29.md) method of an [`NSXPCConnection`](../nsxpcconnection.md) object.

## See Also

### Using standard listeners
- [class func service() -> NSXPCListener](./service%28%29.md)
  Returns the singleton listener used to listen for incoming connections in an XPC service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpclistener/anonymous())*