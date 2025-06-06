# contains(_:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Returns a Boolean value that indicates whether the given element exists in the set.

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
func contains(_ member: Self.Element) -> Bool
```

#### Return Value

`true` if `member` exists in the set; otherwise, `false`.

#### Discussion

This example uses the `contains(_:)` method to test whether an integer is a member of a set of prime numbers.

```swift
let primes: Set = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
let x = 5
if primes.contains(x) {
    print("\(x) is prime!")
} else {
    print("\(x). Not prime.")
}
// Prints "5 is prime!"
```

## Parameters

- `member`: An element to look for in the set.

## See Also

- [associatedtype Element](setalgebra/element.md)
  A type for which the conforming type provides a containment test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/setalgebra/contains(_:))*