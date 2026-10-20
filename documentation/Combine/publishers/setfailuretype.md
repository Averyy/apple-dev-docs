# Publishers.SetFailureType

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

A publisher that appears to send a specified failure type.

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
struct SetFailureType<Upstream, Failure> where Upstream : Publisher, Failure : Error, Upstream.Failure == Never
```

#### Overview

The publisher can’t actually fail with the specified type and finishes normally. Use this publisher type when you need to match the error types for two mismatched publishers.

## Topics

### Creating a set failure type publisher
- [init(upstream: Upstream)](./setfailuretype/init%28upstream%29.md)
  Creates a publisher that appears to send a specified failure type.
### Setting failure type
- [func setFailureType<E>(to: E.Type) -> Publishers.SetFailureType<Upstream, E>](./setfailuretype/setfailuretype%28to%29.md)
  Changes the failure type declared by the upstream publisher.
### Declaring supporting types
- [Publishers.SetFailureType.Output](./setfailuretype/output.md)
  The kind of values published by this publisher.
### Inspecting publisher properties
- [let upstream: Upstream](./setfailuretype/upstream.md)
  The publisher from which this publisher receives elements.
### Comparing publishers
- [static func == (Publishers.SetFailureType<Upstream, Failure>, Publishers.SetFailureType<Upstream, Failure>) -> Bool](./setfailuretype/eqeq%28_,_%29.md)
  Returns a Boolean value that indicates whether two publishers are equivalent.
### Default Implementations
- [Equatable Implementations](./setfailuretype/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Publisher](../publisher.md)

## See Also

### Mapping elements
- [Publishers.Map](./map.md)
  A publisher that transforms all elements from the upstream publisher with a provided closure.
- [Publishers.TryMap](./trymap.md)
  A publisher that transforms all elements from the upstream publisher with a provided error-throwing closure.
- [Publishers.MapError](./maperror.md)
  A publisher that converts any failure from the upstream publisher into a new error.
- [Publishers.Scan](./scan.md)
  A publisher that transforms elements from the upstream publisher by providing the current element to a closure along with the last value returned by the closure.
- [Publishers.TryScan](./tryscan.md)
  A publisher that transforms elements from the upstream publisher by providing the current element to a failable closure along with the last value returned by the closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/setfailuretype)*