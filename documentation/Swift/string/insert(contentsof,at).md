# insert(contentsOf:at:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Inserts a collection of characters at the specified position.

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
mutating func insert<S>(contentsOf newElements: S, at i: String.Index) where S : Collection, S.Element == Character
```

#### Discussion

Calling this method invalidates any existing indices for use with this string.

> **Complexity**: O(*n*), where *n* is the combined length of the string and `newElements`.

## Parameters

- `newElements`: A collection of `Character` elements to insert into the string.
- `i`: A valid index of the string. If `i` is equal to the string’s end index, this methods appends the contents of `newElements` to the string.

## See Also

### Inserting Characters
- [func insert(Character, at: String.Index)](./insert%28_,at%29.md)
  Inserts a new character at the specified position.
- [func insert(Self.Element, at: Self.Index)](./insert%28_,at%29-88yqh.md)
  Inserts a new element into the collection at the specified position.
- [func insert<C>(contentsOf: C, at: Self.Index)](./insert%28contentsof,at%29-rdu9.md)
  Inserts the elements of a sequence into the collection at the specified position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/insert(contentsof:at:))*