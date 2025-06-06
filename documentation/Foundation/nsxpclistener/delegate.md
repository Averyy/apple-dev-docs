# delegate

**Framework**: Foundation  
**Kind**: property

The delegate for the listener.

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
weak var delegate: (any NSXPCListenerDelegate)? { get set }
```

#### Discussion

If no delegate is set, all new connections are rejected. See the documentation for [`NSXPCListenerDelegate`](nsxpclistenerdelegate.md) for implementation details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpclistener/delegate)*