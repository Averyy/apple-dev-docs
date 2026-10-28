# append(_:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Appends the given string to this string.

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
mutating func append(_ other: String)
```

## Discussion

The following example builds a customized greeting by using the `append(_:)` method:

```swift
var greeting = "Hello, "
if let name = getUserName() {
    greeting.append(name)
} else {
    greeting.append("friend")
}
print(greeting)
// Prints "Hello, friend"
```

## Parameters

- `other`: Another string.

## See Also

### Appending Strings and Characters
- [func append(Character)](./append%28_%29-4xi3j.md)
  Appends the given character to the string.
- [func append(contentsOf: String)](./append%28contentsof%29-oxek.md)
- [func append(contentsOf: Substring)](./append%28contentsof%29-9vb4t.md)
- [func append<S>(contentsOf: S)](./append%28contentsof%29-7est5.md)
  Appends the characters in the given sequence to the string.
- [func append<S>(contentsOf: S)](./append%28contentsof%29-9foms.md)
  Adds the elements of a sequence or collection to the end of this collection.
- [func reserveCapacity(Int)](./reservecapacity%28_%29.md)
  Reserves enough space in the string’s underlying storage to store the specified number of ASCII characters.
- [static func + (String, String) -> String](./plus%28_,_%29.md)
- [static func += (inout String, String)](./pluseq%28_,_%29.md)
- [static func + <Other>(Other, Self) -> Self](./plus%28_,_%29-6h59y.md)
  Creates a new collection by concatenating the elements of a sequence and a collection.
- [static func + <Other>(Self, Other) -> Self](./plus%28_,_%29-n329.md)
  Creates a new collection by concatenating the elements of a collection and a sequence.
- [static func + <Other>(Self, Other) -> Self](./plus%28_,_%29-9fm57.md)
  Creates a new collection by concatenating the elements of two collections.
- [static func += <Other>(inout Self, Other)](./pluseq%28_,_%29-676gx.md)
  Appends the elements of a sequence to a range-replaceable collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/append(_:)-4xa8f)*