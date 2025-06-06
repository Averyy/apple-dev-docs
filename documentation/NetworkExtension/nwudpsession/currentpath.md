# currentPath

**Framework**: Network Extension  
**Kind**: property

The current evaluated path for the session’s [`resolvedEndpoint`](nwudpsession/resolvedendpoint.md) property.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var currentPath: NWPath? { get }
```

#### Discussion

Use Key-Value Observing (KVO) to watch for changes to this property. For information about KVO, see [`Key-Value Observing Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

## See Also

- [var endpoint: NWEndpoint](nwudpsession/endpoint.md)
  The destination endpoint with which this session was created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwudpsession/currentpath)*