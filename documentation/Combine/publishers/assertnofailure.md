# Publishers.AssertNoFailure

**Framework**: Combine  
**Kind**: struct

A publisher that raises a fatal error upon receiving any failure, and otherwise republishes all received input.

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
struct AssertNoFailure<Upstream> where Upstream : Publisher
```

#### Overview

Use this function for internal integrity checks that are active during testing but don’t affect performance of shipping code.

## Topics

### Creating an Assert No Failure Publisher
- [init(upstream: Upstream, prefix: String, file: StaticString, line: UInt)](publishers/assertnofailure/init(upstream:prefix:file:line:).md)
  Creates a publisher that raises a fatal error upon receiving any failure, and otherwise republishes all received input.
### Declaring Publisher Topography
- [Publishers.AssertNoFailure.Output](publishers/assertnofailure/output.md)
  The kind of values published by this publisher.
- [Publishers.AssertNoFailure.Failure](publishers/assertnofailure/failure.md)
  The kind of errors this publisher might publish.
### Inspecting Publisher Properties
- [let upstream: Upstream](publishers/assertnofailure/upstream.md)
  The publisher from which this publisher receives elements.
- [let file: StaticString](publishers/assertnofailure/file.md)
  The filename used in the error message.
- [let line: UInt](publishers/assertnofailure/line.md)
  The line number used in the error message.
- [let prefix: String](publishers/assertnofailure/prefix.md)
  The string used at the beginning of the fatal error message.
### Applying Operators
- [Publisher Operators](publishers-assertnofailure-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Publisher Implementations](publishers/assertnofailure/publisher-implementations.md)

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [Publishers.Catch](publishers/catch.md)
  A publisher that handles errors from an upstream publisher by replacing the failed publisher with another publisher.
- [Publishers.TryCatch](publishers/trycatch.md)
  A publisher that handles errors from an upstream publisher by replacing the failed publisher with another publisher or producing a new error.
- [Publishers.Retry](publishers/retry.md)
  A publisher that attempts to recreate its subscription to a failed upstream publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/assertnofailure)*