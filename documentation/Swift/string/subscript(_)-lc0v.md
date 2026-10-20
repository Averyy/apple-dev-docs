# subscript(_:)

**Framework**: Swift  
**Kind**: subscript  
**Role**: Instance Subscript

Accesses the character at the given position.

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
subscript(i: String.Index) -> Character { get }
```

#### Overview

You can use the same indices for subscripting a string and its substring. For example, this code finds the first letter after the first space:

```swift
let str = "Greetings, friend! How are you?"
let firstSpace = str.firstIndex(of: " ") ?? str.endIndex
let substr = str[firstSpace...]
if let nextCapital = substr.firstIndex(where: { $0 >= "A" && $0 <= "Z" }) {
    print("Capital after a space: \(str[nextCapital])")
}
// Prints "Capital after a space: H"
```

## Parameters

- `i`: A valid index of the string. `i` must be less than the string’s end index.

## See Also

### Getting Characters and Bytes
- [var first: Self.Element?](./first.md)
  The first element of the collection.
- [var last: Self.Element?](./last.md)
  The last element of the collection.
- [func randomElement() -> Self.Element?](./randomelement%28%29.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](./randomelement%28using%29.md)
  Returns a random element of the collection, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/subscript(_:)-lc0v)*