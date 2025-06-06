# subscript(_:)

**Framework**: Swift  
**Kind**: subscript

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

- `i`: A valid index of the string.   must be less than the   string’s end index.

## See Also

- [var first: Self.Element?](string/first.md)
  The first element of the collection.
- [var last: Self.Element?](string/last.md)
  The last element of the collection.
- [func randomElement() -> Self.Element?](string/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](string/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/subscript(_:)-lc0v)*