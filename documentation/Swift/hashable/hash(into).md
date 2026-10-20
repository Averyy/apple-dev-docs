# hash(into:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Hashes the essential components of this value by feeding them into the given hasher.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func hash(into hasher: inout Hasher)
```

#### Discussion

Implement this method to conform to the `Hashable` protocol. The components used for hashing must be the same as the components compared in your type’s `==` operator implementation. Call `hasher.combine(_:)` with each of these components.

> ❗ **Important**: In your implementation of `hash(into:)`, don’t call `finalize()` on the `hasher` instance provided, or replace it with a different instance. Doing so may become a compile-time error in the future.

## Parameters

- `hasher`: The hasher to use when combining the components of this instance.

## Default Implementations

### DistributedActor Implementations
- [func hash(into: inout Hasher)](../../Distributed/distributedactor/hash%28into%29.md)
  A distributed actor’s hash and equality is implemented by directly delegating to its [`id`](../../Distributed/distributedactor/id.md).
### Hashable Implementations
- [func hash(into: inout Hasher)](./hash%28into%29-3gv4c.md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [func hash(into: inout Hasher)](./hash%28into%29-86617.md)
  Hashes the elements of the vector using the given hasher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/hashable/hash(into:))*