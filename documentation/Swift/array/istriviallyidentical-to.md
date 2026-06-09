# isTriviallyIdentical(to:)

**Framework**: Swift  
**Kind**: method

Returns a boolean value indicating whether this array is identical to `other`.

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
func isTriviallyIdentical(to other: Array<Element>) -> Bool
```

#### Discussion

Two array values are identical if there is no way to distinguish between them.

For any values `a`, `b`, and `c`:

- `a.isTriviallyIdentical(to: a)` is always `true`. (Reflexivity)
- `a.isTriviallyIdentical(to: b)` implies `b.isTriviallyIdentical(to: a)`. (Symmetry)
- If `a.isTriviallyIdentical(to: b)` and `b.isTriviallyIdentical(to: c)` are both `true`, then `a.isTriviallyIdentical(to: c)` is also `true`. (Transitivity)
- If `a` and `b` are `Equatable`, then `a.isTriviallyIdentical(b)` implies `a == b`. `a == b` does not imply `a.isTriviallyIdentical(b)`

Values produced by copying the same value, with no intervening mutations, compare as identical:

```swift
let d = c
print(c.isTriviallyIdentical(to: d))
// Prints true.
```

Comparing arrays this way includes comparing implementation details that are normally hidden, such as the memory location of any underlying array storage, These details aren’t considered when comparing for equality with the `==` operator. Therefore, identical arrays are guaranteed to compare equal, but not all equal arrays are identical.

> **Note**: O(1)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/istriviallyidentical(to:))*