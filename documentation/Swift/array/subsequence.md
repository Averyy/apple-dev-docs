# Array.SubSequence

**Framework**: Swift  
**Kind**: typealias  
**Role**: Type Alias

A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.

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
typealias SubSequence = ArraySlice<Element>
```

#### Discussion

The default subsequence type for collections that don’t define their own is `Slice`.

## See Also

### Supporting Types
- [typealias Index](./index.md)
  The index type for arrays, `Int`.
- [typealias Indices](./indices.md)
  The type that represents the indices that are valid for subscripting an array, in ascending order.
- [typealias Iterator](./iterator.md)
  The type that allows iteration over an array’s elements.
- [typealias ArrayLiteralElement](./arrayliteralelement.md)
  The type of the elements of an array literal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/subsequence)*