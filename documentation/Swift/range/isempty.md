# isEmpty

**Framework**: Swift  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the range contains no elements.

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
var isEmpty: Bool { get }
```

#### Discussion

An empty `Range` instance has equal lower and upper bounds.

```swift
let empty: Range = 10..<10
print(empty.isEmpty)
// Prints "true"
```

## See Also

### Inspecting a Range
- [let lowerBound: Bound](./lowerbound.md)
  The range’s lower bound.
- [let upperBound: Bound](./upperbound.md)
  The range’s upper bound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/range/isempty)*