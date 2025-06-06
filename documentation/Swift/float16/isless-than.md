# isLess(than:)

**Framework**: Swift  
**Kind**: method

Returns a Boolean value indicating whether this instance is less than the given value.

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
func isLess(than other: Float16) -> Bool
```

#### Return Value

`true` if this value is less than `other`; otherwise, `false`. If either this value or `other` is NaN, the result of this method is `false`.

#### Discussion

This method serves as the basis for the less-than operator (`<`) for floating-point values. Some special cases apply:

- Because NaN compares not less than nor greater than any value, this method returns `false` when called on NaN or when NaN is passed as `other`.
- `-infinity` compares less than all values except for itself and NaN.
- Every value except for NaN and `+infinity` compares less than `+infinity`. let x = 15.0 x.isLess(than: 20.0) // true x.isLess(than: .nan) // false Double.nan.isLess(than: x) // false

The `isLess(than:)` method implements the less-than predicate defined by the [`IEEE 754 specification`](https://developer.apple.comhttp://ieeexplore.ieee.org/servlet/opac?punumber=4610933).

## Parameters

- `other`: The value to compare with this value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float16/isless(than:))*