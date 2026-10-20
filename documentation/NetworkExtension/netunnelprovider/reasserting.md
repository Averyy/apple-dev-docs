# reasserting

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

Indicate to the system that the tunnel is being re-established.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var reasserting: Bool { get set }
```

```objc
@property BOOL reasserting;
```

#### Discussion

The Tunnel Provider should set this property to [`true`](../../Swift/true.md) whenever it starts to reconnect to the tunnel server. Once the Tunnel Provider completes the process of reconnecting it should set this property to [`false`](../../Swift/false.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/netunnelprovider/reasserting)*