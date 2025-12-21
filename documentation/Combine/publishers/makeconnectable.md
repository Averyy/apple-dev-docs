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

### Creating a connectable publisher
- [init(upstream: Upstream)](publishers/makeconnectable/init(upstream:).md)
  Creates a connectable publisher, attached to the provide upstream publisher.
### Declaring supporting types
- [Publishers.MakeConnectable.Output](publishers/makeconnectable/output.md)
  The kind of values published by this publisher.
- [Publishers.MakeConnectable.Failure](publishers/makeconnectable/failure.md)
  The kind of errors this publisher might publish.

## Relationships

### Conforms To
- [ConnectablePublisher](connectablepublisher.md)
- [Publisher](publisher.md)

## See Also

- [Publishers.Autoconnect](publishers/autoconnect.md)
  A publisher that automatically connects to an upstream connectable publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/makeconnectable)*