# Publishers.Autoconnect

**Framework**: Combine  
**Kind**: class

A publisher that automatically connects to an upstream connectable publisher.

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
class Autoconnect<Upstream> where Upstream : ConnectablePublisher
```

#### Overview

This publisher calls [`connect()`](connectablepublisher/connect().md) on the upstream [`ConnectablePublisher`](connectablepublisher.md) when first attached to by a subscriber.

## Topics

### Creating an autoconnect publisher
- [init(upstream: Upstream)](publishers/autoconnect/init(upstream:).md)
  Creates a publisher that automatically connects to an upstream connectable publisher.
### Declaring supporting types
- [Publishers.Autoconnect.Output](publishers/autoconnect/output.md)
  The kind of values published by this publisher.
- [Publishers.Autoconnect.Failure](publishers/autoconnect/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](publishers/autoconnect/upstream.md)
  The publisher from which this publisher receives elements.

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [Publishers.MakeConnectable](publishers/makeconnectable.md)
  A publisher that provides explicit connectability to another publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/autoconnect)*