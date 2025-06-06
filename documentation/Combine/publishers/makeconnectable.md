# Publishers.MakeConnectable

**Framework**: Combine  
**Kind**: struct

A publisher that provides explicit connectability to another publisher.

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
struct MakeConnectable<Upstream> where Upstream : Publisher
```

## Mentions

- [Controlling Publishing with Connectable Publishers](controlling-publishing-with-connectable-publishers.md)

#### Overview

[`Publishers.MakeConnectable`](publishers/makeconnectable.md) is a [`ConnectablePublisher`](connectablepublisher.md), which allows you to perform configuration before publishing any elements. Call [`connect()`](connectablepublisher/connect().md) on this publisher when you want to attach to its upstream publisher and start producing elements.

Use the [`makeConnectable()`](publisher/makeconnectable().md) operator to wrap an upstream publisher with an instance of this publisher.

## Topics

### Creating a Connectable Publisher
- [init(upstream: Upstream)](publishers/makeconnectable/init(upstream:).md)
  Creates a connectable publisher, attached to the provide upstream publisher.
### Declaring Publisher Topography
- [Publishers.MakeConnectable.Output](publishers/makeconnectable/output.md)
  The kind of values published by this publisher.
- [Publishers.MakeConnectable.Failure](publishers/makeconnectable/failure.md)
  The kind of errors this publisher might publish.
### Performing Explicit Connections
- [func connect() -> any Cancellable](publishers/makeconnectable/connect.md)
  Connects to the publisher, allowing it to produce elements, and returns an instance with which to cancel publishing.
### Connecting Automatically
- [func autoconnect() -> Publishers.Autoconnect<Self>](publishers/makeconnectable/autoconnect.md)
  Automates the process of connecting or disconnecting from this connectable publisher.
### Applying Operators
- [Publisher Operators](publishers-makeconnectable-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [ConnectablePublisher Implementations](publishers/makeconnectable/connectablepublisher-implementations.md)
- [Publisher Implementations](publishers/makeconnectable/publisher-implementations.md)

## Relationships

### Conforms To
- [ConnectablePublisher](connectablepublisher.md)
- [Publisher](publisher.md)

## See Also

- [Publishers.Autoconnect](publishers/autoconnect.md)
  A publisher that automatically connects to an upstream connectable publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/makeconnectable)*