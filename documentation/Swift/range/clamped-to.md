# clamped(to:)

**Framework**: Swift  
**Kind**: method

Returns a copy of this range clamped to the given limiting range.

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
func clamped(to limits: Range<Bound>) -> Range<Bound>
```

#### Return Value

A new range clamped to the bounds of `limits`.

#### Discussion

The bounds of the result are always limited to the bounds of `limits`. For example:

```swift
let x: Range = 0..<20
print(x.clamped(to: 10..<1000))
// Prints "10..<20"
```

If the two ranges do not overlap, the result is an empty range within the bounds of `limits`.

```swift
let y: Range = 0..<5
print(y.clamped(to: 10..<1000))
// Prints "10..<10"
```

## Parameters

- `limits`: The range to clamp the bounds of this range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/range/clamped(to:))*