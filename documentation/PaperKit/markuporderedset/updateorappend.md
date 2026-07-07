# updateOrAppend(_:)

**Framework**: PaperKit  
**Kind**: method

Adds the given element to the set unconditionally, either appending it to the set, or replacing an existing value if one with the same id is present.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@discardableResult
mutating func updateOrAppend(_ item: MarkupOrderedSet.Element) -> MarkupOrderedSet.Element?
```

#### Return Value

The element this operation replaced, or `nil` if the operation appended the value to the end of the collection.

## Parameters

- `item`: The value to append or replace.

## See Also

- [func append(MarkupOrderedSet.Element) -> (inserted: Bool, index: Int)](markuporderedset/append(_:).md)
  Appends a new member to the end of the set, if the set doesn’t already contain it.
- [func append(contentsOf: some Sequence<any Markup>)](markuporderedset/append(contentsof:).md)
  Appends the contents of a sequence to the end of the set, excluding elements that are already members.
- [func insert(MarkupOrderedSet.Element, at: Int) -> (inserted: Bool, index: Int)](markuporderedset/insert(_:at:).md)
  Inserts a new member at the specified index, if the set doesn’t already contain it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markuporderedset/updateorappend(_:))*