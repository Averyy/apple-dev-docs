# draggedItemIDs(for:)

**Framework**: SwiftUI  
**Kind**: method

Provides an array of identifiers of the currently dragged items in a case when the items conform to the `Identifiable` protocol, or identifiers were provided to SwiftUI separately.

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

Parameter type: The type of the identifiers. Returns: The array with the identifiers of the dragged items if provided. Returns an empty array if no dragged identifiers of a given type exist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dragsession/draggeditemids(for:))*