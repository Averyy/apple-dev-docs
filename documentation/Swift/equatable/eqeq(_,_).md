# ==(_:_:)

**Framework**: Swift  
**Kind**: op  
**Role**: Operator  
**Required**: Yes

Returns a Boolean value indicating whether two values are equal.

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
static func == (lhs: borrowing Self, rhs: borrowing Self) -> Bool
```

#### Discussion

Equality is the inverse of inequality. For any values `a` and `b`, `a == b` implies that `a != b` is `false`.

## Parameters

- `lhs`: A value to compare.
- `rhs`: Another value to compare.

## Default Implementations

### DistributedActor Implementations
- [static func == (Self, Self) -> Bool](../../Distributed/distributedactor/eqeq%28_,_%29.md)
  A distributed actor’s hash and equality is implemented by directly delegating to its [`id`](../../Distributed/distributedactor/id.md).
### Equatable Implementations
- [static func == (Self, Self) -> Bool](./eqeq%28_,_%29-1xq7p.md)
  Returns a Boolean value indicating whether two values are equal.
- [static func == (Self, Self) -> Bool](./eqeq%28_,_%29-3ngto.md)
  Returns a Boolean value indicating whether two values are equal.
- [static func == (Self, Self) -> Bool](./eqeq%28_,_%29-6673q.md)
  Returns a Boolean value indicating whether two vectors are equal.
- [static func == <Other>(Self, Other) -> Bool](./eqeq%28_,_%29-7do7a.md)
  Returns a Boolean value indicating whether the two given values are equal.
- [static func == <RHS>(Self, RHS) -> Bool](./eqeq%28_,_%29-7k1nz.md)

## See Also

### Equatable Requirements
- [static func != (borrowing Self, borrowing Self) -> Bool](./noteq%28_,_%29.md)
  Returns a Boolean value indicating whether two values are not equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/equatable/==(_:_:))*