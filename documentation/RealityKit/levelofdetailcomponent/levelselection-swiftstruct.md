# LevelOfDetailComponent.LevelSelection

**Framework**: RealityKit  
**Kind**: struct

Controls whether LOD selection is automatic or manually overridden.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct LevelSelection
```

## Topics

### Type Properties
- [static let automatic: LevelOfDetailComponent.LevelSelection](levelofdetailcomponent/levelselection-swift.struct/automatic.md)
  Use automatic LOD selection based on the configured strategy.
### Type Methods
- [static func fixed(Int) -> LevelOfDetailComponent.LevelSelection](levelofdetailcomponent/levelselection-swift.struct/fixed(_:).md)
  Override automatic selection and always display the specified level index.

## See Also

- [var strategy: LevelOfDetailComponent.SelectionStrategy](levelofdetailcomponent/strategy.md)
- [LevelOfDetailComponent.SelectionStrategy](levelofdetailcomponent/selectionstrategy.md)
  The strategy used to select which detail level to display.
- [var levelSelection: LevelOfDetailComponent.LevelSelection](levelofdetailcomponent/levelselection-swift.property.md)
  The level selection mode. Defaults to automatic selection based on the strategy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/levelofdetailcomponent/levelselection-swift.struct)*