# flatMap(maxPublishers:_:)

**Framework**: Swift  
**Kind**: method

Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func flatMap<P>(maxPublishers: Subscribers.Demand = .unlimited, _ transform: @escaping (Self.Output) -> P) -> Publishers.FlatMap<P, Publishers.SetFailureType<Self, P.Failure>> where P : Publisher
```

#### Return Value

A publisher that transforms elements from an upstream  publisher into a publisher of that element’s type.

## Parameters

- `maxPublishers`: Specifies the maximum number of concurrent publisher subscriptions, or   if unspecified.
- `transform`: A closure that takes an element as a parameter and returns a publisher that produces elements of that type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/optional/publisher-swift.struct/flatmap(maxpublishers:_:)-9dqz0)*