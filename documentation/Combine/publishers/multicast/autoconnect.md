# autoconnect()

**Framework**: Combine  
**Kind**: method

Automates the process of connecting or disconnecting from this connectable publisher.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func autoconnect() -> Publishers.Autoconnect<Self>
```

#### Return Value

A publisher which automatically connects to its upstream connectable publisher.

#### Discussion

Use [`autoconnect()`](connectablepublisher/autoconnect().md) to simplify working with [`ConnectablePublisher`](connectablepublisher.md) instances, such as [`Timer.TimerPublisher`](https://developer.apple.com/documentation/Foundation/Timer/TimerPublisher) in the Foundation framework.

In the following example, the [`publish(every:tolerance:on:in:options:)`](https://developer.apple.com/documentation/Foundation/Timer/publish(every:tolerance:on:in:options:)) operator creates a [`Timer.TimerPublisher`](https://developer.apple.com/documentation/Foundation/Timer/TimerPublisher), which is a [`ConnectablePublisher`](connectablepublisher.md). As a result, subscribers don’t receive any values until after a call to [`connect()`](connectablepublisher/connect().md). For convenience when working with a single subscriber, the [`autoconnect()`](connectablepublisher/autoconnect().md) operator performs the [`connect()`](connectablepublisher/connect().md) call when attached to by the subscriber.

```swift
cancellable = Timer.publish(every: 1, on: .main, in: .default)
    .autoconnect()
    .sink { date in
        print ("Date now: \(date)")
    }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/multicast/autoconnect())*