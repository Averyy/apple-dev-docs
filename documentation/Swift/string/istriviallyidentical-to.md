# isTriviallyIdentical(to:)

**Framework**: Swift  
**Kind**: method

Returns a boolean value indicating whether this string is identical to `other`.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func isTriviallyIdentical(to other: String) -> Bool
```

#### Discussion

Two string values are identical if there is no way to distinguish between them.

For any values `a`, `b`, and `c`:

- `a.isTriviallyIdentical(to: a)` is always `true`. (Reflexivity)
- `a.isTriviallyIdentical(to: b)` implies `b.isTriviallyIdentical(to: a)`. (Symmetry)
- If `a.isTriviallyIdentical(to: b)` and `b.isTriviallyIdentical(to: c)` are both `true`, then `a.isTriviallyIdentical(to: c)` is also `true`. (Transitivity)
- `a.isTriviallyIdentical(b)` implies `a == b`. `a == b` does not imply `a.isTriviallyIdentical(b)`

Values produced by copying the same value, with no intervening mutations, will compare identical:

```swift
let d = c
print(c.isTriviallyIdentical(to: d))
// Prints true
```

Comparing strings this way includes comparing (normally) hidden implementation details such as the memory location of any underlying string storage object. Therefore, identical strings are guaranteed to compare equal with `==`, but not all equal strings are considered identical.

> **Note**: O(1)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/istriviallyidentical(to:))*