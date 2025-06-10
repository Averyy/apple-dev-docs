# draggedItemIDs(for:)

**Framework**: SwiftUI  
**Kind**: method

Provides an array of identifiers of the currently dragged items if available.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func draggedItemIDs<ItemID>(for type: ItemID.Type) -> [ItemID] where ItemID : Hashable
```

#### Discussion

If drag started within the application, the dragged items have identifiers, and SwiftUI has access to these identifiers, you can access them using this method.

Parameter type: The type of the identifiers. Returns: The array with the identifiers of the dragged items if provided. Returns an empty array if there are no dragged identifiers of a given type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dropsession/localsession-swift.struct/draggeditemids(for:))*