# Publishers.Print

**Framework**: Combine  
**Kind**: struct

A publisher that prints log messages for all publishing events, optionally prefixed with a given string.

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
struct Print<Upstream> where Upstream : Publisher
```

#### Overview

This publisher prints log messages when receiving the following events:

- subscription
- value
- normal completion
- failure
- cancellation

## Topics

### Creating a print publisher
- [init(upstream: Upstream, prefix: String, to: (any TextOutputStream)?)](publishers/print/init(upstream:prefix:to:).md)
  Creates a publisher that prints log messages for all publishing events.
### Declaring supporting types
- [Publishers.Print.Output](publishers/print/output.md)
  The kind of values published by this publisher.
- [Publishers.Print.Failure](publishers/print/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](publishers/print/upstream.md)
  The publisher from which this publisher receives elements.
- [let prefix: String](publishers/print/prefix.md)
  A string with which to prefix all log messages.
- [let stream: (any TextOutputStream)?](publishers/print/stream.md)

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [Publishers.Breakpoint](publishers/breakpoint.md)
  A publisher that raises a debugger signal when a provided closure needs to stop the process in the debugger.
- [Publishers.HandleEvents](publishers/handleevents.md)
  A publisher that performs the specified closures when publisher events occur.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/print)*