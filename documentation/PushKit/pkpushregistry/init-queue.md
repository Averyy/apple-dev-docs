# init(queue:)

**Framework**: PushKit  
**Kind**: init

Creates a push registry with the specified dispatch queue.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(queue: dispatch_queue_t?)
```

#### Return Value

A `PKPushRegistry` object that you can use to register for push tokens and use to receive notifications.

## Parameters

- `queue`: The dispatch queue on which to execute the delegate methods. It is recommended that you specify a serial queue for this parameter. Specify   to execute the delegate methods on the app’s main queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushkit/pkpushregistry/init(queue:))*