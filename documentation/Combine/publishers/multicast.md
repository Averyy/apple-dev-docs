# Publishers.Multicast

**Framework**: Combine  
**Kind**: class

A publisher that uses a subject to deliver elements to multiple subscribers.

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
final class Multicast<Upstream, SubjectType> where Upstream : Publisher, SubjectType : Subject, Upstream.Failure == SubjectType.Failure, Upstream.Output == SubjectType.Output
```

## Mentions

- [Controlling Publishing with Connectable Publishers](controlling-publishing-with-connectable-publishers.md)

#### Overview

Use a multicast publisher when you have multiple downstream subscribers, but you want upstream publishers to only process one [`receive(_:)`](subscriber/receive(_:).md) call per event.

## Topics

### Creating a multicast publisher
- [init(upstream: Upstream, createSubject: () -> SubjectType)](publishers/multicast/init(upstream:createsubject:).md)
  Creates a multicast publisher that applies a closure to create a subject that delivers elements to subscribers.
### Declaring supporting types
- [Publishers.Multicast.Output](publishers/multicast/output.md)
  The kind of values published by this publisher.
- [Publishers.Multicast.Failure](publishers/multicast/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](publishers/multicast/upstream.md)
  The publisher from which this publisher receives its elements.
- [let createSubject: () -> SubjectType](publishers/multicast/createsubject.md)
  A closure that returns a subject each time a subscriber attaches to the multicast publisher.

## Relationships

### Conforms To
- [ConnectablePublisher](connectablepublisher.md)
- [Publisher](publisher.md)

## See Also

- [Publishers.Share](publishers/share.md)
  A publisher that shares the output of an upstream publisher with multiple subscribers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/multicast)*