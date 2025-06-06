# endIndex

**Framework**: Swift  
**Kind**: property

The array’s “past the end” position—that is, the position one greater than the last valid subscript argument.

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
var endIndex: Int { get }
```

#### Discussion

When you need a range that includes the last element of an array, use the half-open range operator (`..<`) with `endIndex`. The `..<` operator creates a range that doesn’t include the upper bound, so it’s always safe to use with `endIndex`. For example:

```swift
let numbers = [10, 20, 30, 40, 50]
if let i = numbers.firstIndex(of: 30) {
    print(numbers[i ..< numbers.endIndex])
}
// Prints "[30, 40, 50]"
```

If the array is empty, `endIndex` is equal to `startIndex`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/arrayslice/endindex)*