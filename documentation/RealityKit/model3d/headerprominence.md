# headerProminence(_:)

**Framework**: RealityKit  
**Kind**: method

Sets the header prominence for this view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func headerProminence(_ prominence: Prominence) -> some View
```

#### Discussion

In the following example, the section header appears with increased prominence:

```None
List {
    Section(header: Text("Header")) {
        Text("Row")
    }
    .headerProminence(.increased)
}
.listStyle(.insetGrouped)
```

## Parameters

- `prominence`: The prominence to apply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/model3d/headerprominence(_:))*