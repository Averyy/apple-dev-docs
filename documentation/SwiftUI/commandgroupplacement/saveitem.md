# saveItem

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

Placement for commands that save open documents and close windows.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static let saveItem: CommandGroupPlacement
```

#### Discussion

By default, this group includes the following commands in macOS:

- Close
- Save
- Save As/Duplicate
- Revert to Saved

## See Also

### File manipulation
- [static let importExport: CommandGroupPlacement](./importexport.md)
  Placement for commands that relate to importing and exporting data using formats that the app doesn’t natively support.
- [static let newItem: CommandGroupPlacement](./newitem.md)
  Placement for commands that create different kinds of documents.
- [static let printItem: CommandGroupPlacement](./printitem.md)
  Placement for commands related to printing app content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/commandgroupplacement/saveitem)*