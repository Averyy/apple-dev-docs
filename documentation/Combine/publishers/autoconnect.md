# Publishers.Autoconnect

**Framework**: Combine  
**Kind**: class  
**Role**: Class

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

This publisher calls [`connect()`](../connectablepublisher/connect%28%29.md) on the upstream [`ConnectablePublisher`](../connectablepublisher.md) when first attached to by a subscriber.

## Topics

### Creating an autoconnect publisher
- [init(upstream: Upstream)](./autoconnect/init%28upstream%29.md)
  Creates a publisher that automatically connects to an upstream connectable publisher.
### Declaring supporting types
- [Publishers.Autoconnect.Output](./autoconnect/output.md)
  The kind of values published by this publisher.
- [Publishers.Autoconnect.Failure](./autoconnect/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](./autoconnect/upstream.md)
  The publisher from which this publisher receives elements.

## Relationships

### Conforms To
- [Publisher](../publisher.md)

## See Also

### Using explicit publisher connections
- [Publishers.MakeConnectable](./makeconnectable.md)
  A publisher that provides explicit connectability to another publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/autoconnect)*