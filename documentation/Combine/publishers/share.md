# Publishers.Share

**Framework**: Combine  
**Kind**: class

A publisher that shares the output of an upstream publisher with multiple subscribers.

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
final class Share<Upstream> where Upstream : Publisher
```

#### Overview

This publisher type supports multiple subscribers, all of whom receive unchanged elements and completion states from the upstream publisher.

> 💡 **Tip**: [`Publishers.Share`](publishers/share.md) is effectively a combination of the [`Publishers.Multicast`](publishers/multicast.md) and [`PassthroughSubject`](passthroughsubject.md) publishers, with an implicit [`autoconnect()`](connectablepublisher/autoconnect().md).

Be aware that [`Publishers.Share`](publishers/share.md) is a class rather than a structure like most other publishers. Use this type when you need a publisher instance that uses reference semantics.

## Topics

### Creating a share publisher
- [init(upstream: Upstream)](publishers/share/init(upstream:).md)
  Creates a publisher that shares the output of an upstream publisher with multiple subscribers.
### Declaring supporting types
- [Publishers.Share.Output](publishers/share/output.md)
  The kind of values published by this publisher.
- [Publishers.Share.Failure](publishers/share/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](publishers/share/upstream.md)
  The publisher from which this publisher receives elements.
### Comparing publishers
- [static func == (Publishers.Share<Upstream>, Publishers.Share<Upstream>) -> Bool](publishers/share/==(_:_:).md)
  Returns a Boolean value that indicates whether two publishers are equivalent.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Publisher](publisher.md)

## See Also

- [Publishers.Multicast](publishers/multicast.md)
  A publisher that uses a subject to deliver elements to multiple subscribers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/share)*