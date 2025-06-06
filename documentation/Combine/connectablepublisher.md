# ConnectablePublisher

**Framework**: Combine  
**Kind**: protocol

A publisher that provides an explicit means of connecting and canceling publication.

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
protocol ConnectablePublisher<Output, Failure> : Publisher
```

## Mentions

- [Controlling Publishing with Connectable Publishers](controlling-publishing-with-connectable-publishers.md)
- [Replacing Foundation Timers with Timer Publishers](replacing-foundation-timers-with-timer-publishers.md)

#### Overview

Use a [`ConnectablePublisher`](connectablepublisher.md) when you need to perform additional configuration or setup prior to producing any elements.

This publisher doesn’t produce any elements until you call its [`connect()`](connectablepublisher/connect().md) method.

Use [`makeConnectable()`](publisher/makeconnectable().md) to create a [`ConnectablePublisher`](connectablepublisher.md) from any publisher whose failure type is [`Never`](https://developer.apple.com/documentation/Swift/Never).

## Topics

### Performing Explicit Connections
- [func connect() -> any Cancellable](connectablepublisher/connect.md)
  Connects to the publisher, allowing it to produce elements, and returns an instance with which to cancel publishing.
### Connecting Automatically
- [func autoconnect() -> Publishers.Autoconnect<Self>](connectablepublisher/autoconnect.md)
  Automates the process of connecting or disconnecting from this connectable publisher.

## Relationships

### Inherits From
- [Publisher](publisher.md)
### Conforming Types
- [Publishers.MakeConnectable](publishers/makeconnectable.md)
- [Publishers.Multicast](publishers/multicast.md)

## See Also

- [Controlling Publishing with Connectable Publishers](controlling-publishing-with-connectable-publishers.md)
  Coordinate when publishers start sending elements to subscribers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/connectablepublisher)*