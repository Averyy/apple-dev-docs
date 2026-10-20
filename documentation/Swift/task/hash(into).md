# hash(into:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Hashes the essential components of this value by feeding them into the given hasher.

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
func hash(into hasher: inout Hasher)
```

Available when `Success` conforms to `Sendable` and `Failure` conforms to `Error`.

#### Discussion

Implement this method to conform to the `Hashable` protocol. The components used for hashing must be the same as the components compared in your type’s `==` operator implementation. Call `hasher.combine(_:)` with each of these components.

> ❗ **Important**: In your implementation of `hash(into:)`, don’t call `finalize()` on the `hasher` instance provided, or replace it with a different instance. Doing so may become a compile-time error in the future.

## Parameters

- `hasher`: The hasher to use when combining the components of this instance.

## See Also

### Comparing Tasks
- [static func == (Task<Success, Failure>, Task<Success, Failure>) -> Bool](./eqeq%28_,_%29.md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (borrowing Self, borrowing Self) -> Bool](./noteq%28_,_%29.md)
  Returns a Boolean value indicating whether two values are not equal.
- [var hashValue: Int](./hashvalue.md)
  The hash value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task/hash(into:))*