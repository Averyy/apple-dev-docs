# onInsert(of:perform:)

**Framework**: SwiftUI  
**Kind**: method

Sets the insert action for the dynamic table rows.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func onInsert(of supportedContentTypes: [UTType], perform action: @escaping (Int, [NSItemProvider]) -> Void) -> ModifiedContent<Self, OnInsertTableRowModifier>
```

#### Return Value

A view that calls `action` when inserting elements into the original view.

## Parameters

- `supportedContentTypes`: An array of universal type identifiers types that the rows supports.
- `action`: A closure that SwiftUI invokes when adding elements to   the collection of rows.   The closure takes two arguments. The first argument is the   offset relative to the dynamic view’s underlying collection of data.   The second argument is an array of     items that represents the data that you want to insert.

## See Also

- [struct OnInsertTableRowModifier](oninserttablerowmodifier.md)
  A table row modifier that adds the ability to insert data in some base row content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dynamictablerowcontent/oninsert(of:perform:))*