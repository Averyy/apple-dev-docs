# isTotallyOrdered(belowOrEqualTo:)

**Framework**: Swift  
**Kind**: method

Returns a Boolean value indicating whether this instance should precede or tie positions with the given value in an ascending sort.

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
func isTotallyOrdered(belowOrEqualTo other: Self) -> Bool
```

#### Return Value

`true` if this value is ordered below or the same as `other` in a total ordering of the floating-point type; otherwise, `false`.

#### Discussion

This relation is a refinement of the less-than-or-equal-to operator (`<=`) that provides a total order on all values of the type, including signed zeros and NaNs.

The following example uses `isTotallyOrdered(belowOrEqualTo:)` to sort an array of floating-point values, including some that are NaN:

```swift
var numbers = [2.5, 21.25, 3.0, .nan, -9.5]
numbers.sort { !$1.isTotallyOrdered(belowOrEqualTo: $0) }
print(numbers)
// Prints "[-9.5, 2.5, 3.0, 21.25, nan]"
```

The `isTotallyOrdered(belowOrEqualTo:)` method implements the total order relation as defined by the [`IEEE 754 specification`](https://developer.apple.comhttp://ieeexplore.ieee.org/servlet/opac?punumber=4610933).

## Parameters

- `other`: A floating-point value to compare to this value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float16/istotallyordered(beloworequalto:))*