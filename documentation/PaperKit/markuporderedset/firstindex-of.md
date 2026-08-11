# firstIndex(of:)

**Framework**: PaperKit  
**Kind**: method

Returns the index of the given element in the set, or `nil` if the element is not a member of the set.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func firstIndex(of element: MarkupOrderedSet.Element) -> Int?
```

#### Discussion

`MarkupOrderedSet` members are always unique, so the first index of an element is always the same as its last index.

## See Also

- [func contains(MarkupOrderedSet.Element) -> Bool](markuporderedset/contains(_:).md)
  Returns a Boolean value that indicates whether the given element exists in the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markuporderedset/firstindex(of:))*