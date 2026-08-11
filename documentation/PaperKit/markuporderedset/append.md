# append(_:)

**Framework**: PaperKit  
**Kind**: method

Appends a new member to the end of the set, if the set doesn’t already contain it.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@discardableResult
mutating func append(_ item: MarkupOrderedSet.Element) -> (inserted: Bool, index: Int)
```

#### Return Value

A pair (`inserted`, `index`), where inserted is a Boolean value indicating whether the operation added a new element, and `index` is the index of `item` in the resulting set.

## Parameters

- `item`: The element to add to the set.

## See Also

- [func append(contentsOf: some Sequence<any Markup>)](markuporderedset/append(contentsof:).md)
  Appends the contents of a sequence to the end of the set, excluding elements that are already members.
- [func insert(MarkupOrderedSet.Element, at: Int) -> (inserted: Bool, index: Int)](markuporderedset/insert(_:at:).md)
  Inserts a new member at the specified index, if the set doesn’t already contain it.
- [func updateOrAppend(MarkupOrderedSet.Element) -> MarkupOrderedSet.Element?](markuporderedset/updateorappend(_:).md)
  Adds the given element to the set unconditionally, either appending it to the set, or replacing an existing value if one with the same id is present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markuporderedset/append(_:))*