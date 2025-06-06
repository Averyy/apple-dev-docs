# numberOfItems(inSection:)

**Framework**: AppKit  
**Kind**: method

Returns the number of items in the specified section.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func numberOfItems(inSection section: Int) -> Int
```

#### Return Value

The number of items in the section.

#### Discussion

Use this method to get the number of items currently displayed by the collection view for the specified section. Do not call the methods of the data source to get this information.

## Parameters

- `section`: The index of the section whose item count you want. This index is 0-based.

## See Also

- [var numberOfSections: Int](nscollectionview/numberofsections.md)
  The number of sections in the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/numberofitems(insection:))*