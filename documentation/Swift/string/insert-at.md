# insert(_:at:)

**Framework**: Swift  
**Kind**: method

Inserts a new character at the specified position.

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
mutating func insert(_ newElement: Character, at i: String.Index)
```

#### Discussion

Calling this method invalidates any existing indices for use with this string.

> **Note**: O(), where  is the length of the string.

O(), where  is the length of the string.

## Parameters

- `newElement`: The new character to insert into the string.
- `i`: A valid index of the string. If   is equal to the string’s end   index, this methods appends   to the string.

## See Also

- [func insert(Self.Element, at: Self.Index)](string/insert(_:at:)-88yqh.md)
  Inserts a new element into the collection at the specified position.
- [func insert<C>(contentsOf: C, at: Self.Index)](string/insert(contentsof:at:)-rdu9.md)
  Inserts the elements of a sequence into the collection at the specified position.
- [func insert<S>(contentsOf: S, at: String.Index)](string/insert(contentsof:at:).md)
  Inserts a collection of characters at the specified position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/insert(_:at:))*