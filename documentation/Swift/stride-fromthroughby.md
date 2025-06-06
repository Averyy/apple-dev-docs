# stride(from:through:by:)

**Framework**: Swift  
**Kind**: func

Returns a sequence from a starting value toward, and possibly including, an end value, stepping by the specified amount.

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
func stride<T>(from start: T, through end: T, by stride: T.Stride) -> StrideThrough<T> where T : Strideable
```

#### Return Value

A sequence from `start` toward, and possibly including, `end`. Each value in the sequence is separated by `stride`.

#### Discussion

You can use this function to stride over values of any type that conforms to the `Strideable` protocol, such as integers or floating-point types. Starting with `start`, each successive value of the sequence adds `stride` until the next value would be beyond `end`.

```swift
for radians in stride(from: 0.0, through: .pi * 2, by: .pi / 2) {
    let degrees = Int(radians * 180 / .pi)
    print("Degrees: \(degrees), radians: \(radians)")
}
// Degrees: 0, radians: 0.0
// Degrees: 90, radians: 1.5707963267949
// Degrees: 180, radians: 3.14159265358979
// Degrees: 270, radians: 4.71238898038469
// Degrees: 360, radians: 6.28318530717959
```

You can use `stride(from:through:by:)` to create a sequence that strides upward or downward. Pass a negative value as `stride` to create a sequence from a higher start to a lower end:

```swift
for countdown in stride(from: 3, through: 1, by: -1) {
    print("\(countdown)...")
}
// 3...
// 2...
// 1...
```

The value you pass as `end` is not guaranteed to be included in the sequence. If stepping from `start` by `stride` does not produce `end`, the last value in the sequence will be one step before going beyond `end`.

```swift
for multipleOfThree in stride(from: 3, through: 10, by: 3) {
    print(multipleOfThree)
}
// 3
// 6
// 9
```

If you pass a value as `stride` that moves away from `end`, the sequence contains no values.

```swift
for x in stride(from: 0, through: 10, by: -1) {
    print(x)
}
// Nothing is printed.
```

## Parameters

- `start`: The starting value to use for the sequence. If the sequence   contains any values, the first one is  .
- `end`: An end value to limit the sequence.   is an element of   the resulting sequence if and only if it can be produced from     using steps of  .
- `stride`: The amount to step by with each iteration. A positive    iterates upward; a negative   iterates downward.

## See Also

- [func stride<T>(from: T, to: T, by: T.Stride) -> StrideTo<T>](stride(from:to:by:).md)
  Returns a sequence from a starting value to, but not including, an end value, stepping by the specified amount.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/stride(from:through:by:))*