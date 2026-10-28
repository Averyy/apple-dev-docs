# endpoint

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns an endpoint object that may be sent over an existing connection.

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
var endpoint: NSXPCListenerEndpoint { get }
```

```objc
@property (retain, readonly) NSXPCListenerEndpoint * endpoint;
```

## Discussion

The receiver of the endpoint can use this object to create a new connection to this [`NSXPCListener`](../nsxpclistener.md) object. The resulting `NSXPCListenerEndpoint` object uniquely names this listener object across connections.

## See Also

### Related Documentation
- [Daemons and Services Programming Guide](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/Introduction.html#//apple_ref/doc/uid/10000172i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpclistener/endpoint)*