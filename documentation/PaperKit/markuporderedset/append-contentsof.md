# append(contentsOf:)

**Framework**: PaperKit  
**Kind**: method

Appends the contents of a sequence to the end of the set, excluding elements that are already members.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
mutating func append(contentsOf elements: some Sequence<any Markup>)
```

## Parameters

- `elements`: A finite sequence of elements to append.

## See Also

- [func append(MarkupOrderedSet.Element) -> (inserted: Bool, index: Int)](markuporderedset/append(_:).md)
  Appends a new member to the end of the set, if the set doesn’t already contain it.
- [func insert(MarkupOrderedSet.Element, at: Int) -> (inserted: Bool, index: Int)](markuporderedset/insert(_:at:).md)
  Inserts a new member at the specified index, if the set doesn’t already contain it.
- [func updateOrAppend(MarkupOrderedSet.Element) -> MarkupOrderedSet.Element?](markuporderedset/updateorappend(_:).md)
  Adds the given element to the set unconditionally, either appending it to the set, or replacing an existing value if one with the same id is present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markuporderedset/append(contentsof:))*