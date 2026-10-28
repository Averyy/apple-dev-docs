# advanced(by:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a value that is offset the specified distance from this value.

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
func advanced(by n: Self.Stride) -> Self
```

## Return Value

A value that is offset from this value by `n`.

## Discussion

Use the `advanced(by:)` method in generic code to offset a value by a specified distance. If you’re working directly with numeric values, use the addition operator (`+`) instead of this method.

```swift
func addOne<T: Strideable>(to x: T) -> T
    where T.Stride: ExpressibleByIntegerLiteral
{
    return x.advanced(by: 1)
}

let x = addOne(to: 5)
// x == 6
let y = addOne(to: 3.5)
// y = 4.5
```

If this type’s `Stride` type conforms to `BinaryInteger`, then for a value `x`, a distance `n`, and a value `y = x.advanced(by: n)`, `x.distance(to: y) == n`. Using this method with types that have a noninteger `Stride` may result in an approximation. If the result of advancing by `n` is not representable as a value of this type, then a runtime error may occur.

> **Complexity**: O(1)

## Parameters

- `n`: The distance to advance this value.

## Default Implementations

### Strideable Implementations
- [func advanced(by: Int) -> Self](./advanced%28by%29-9b2es.md)
  Returns a value that is offset the specified distance from this value.

## See Also

### Getting an Offset Value
- [static func + (Self, Self.Stride) -> Self](./plus%28_,_%29-8m1px.md)
- [static func + (Self.Stride, Self) -> Self](./plus%28_,_%29-94mlm.md)
- [static func - (Self, Self.Stride) -> Self](./minus%28_,_%29-1kjns.md)
- [static func - (Self, Self) -> Self.Stride](./minus%28_,_%29-2mot7.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/strideable/advanced(by:))*