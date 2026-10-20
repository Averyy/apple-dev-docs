# OnInsertTableRowModifier

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A table row modifier that adds the ability to insert data in some base row content.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency struct OnInsertTableRowModifier
```

## Topics

### Instance Properties
- [var body: some _TableRowContentModifier](./oninserttablerowmodifier/body-swift.property.md)
### Type Aliases
- [OnInsertTableRowModifier.Body](./oninserttablerowmodifier/body-swift.typealias.md)

## See Also

### Inserting rows
- [func onInsert(of: [UTType], perform: (Int, [NSItemProvider]) -> Void) -> ModifiedContent<Self, OnInsertTableRowModifier>](./dynamictablerowcontent/oninsert%28of,perform%29.md)
  Sets the insert action for the dynamic table rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/oninserttablerowmodifier)*