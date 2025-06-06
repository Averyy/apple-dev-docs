# init(base:bounds:)

**Framework**: Swift  
**Kind**: init

Creates a view into the given collection that allows access to elements within the specified range.

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
init(base: Base, bounds: Range<Base.Index>)
```

#### Discussion

It is unusual to need to call this method directly. Instead, create a slice of a collection by using the collection’s range-based subscript or by using methods that return a subsequence.

```swift
let singleDigits = 0...9
let subSequence = singleDigits.dropFirst(5)
print(Array(subSequence))
// Prints "[5, 6, 7, 8, 9]"
```

In this example, the expression `singleDigits.dropFirst(5))` is equivalent to calling this initializer with `singleDigits` and a range covering the last five items of `singleDigits.indices`.

## Parameters

- `base`: The collection to create a view into.
- `bounds`: The range of indices to allow access to in the new slice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/slice/init(base:bounds:))*