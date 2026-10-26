# hash(into:)

**Framework**: Distributed  
**Kind**: method  
**Role**: Instance Method

A distributed actor’s hash and equality is implemented by directly delegating to its [`id`](./id.md).

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
nonisolated
func hash(into hasher: inout Hasher)
```

#### Discussion

For more details see the “Hashable and Identifiable conformance” section of [`DistributedActor`](../distributedactor.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/distributedactor/hash(into:))*