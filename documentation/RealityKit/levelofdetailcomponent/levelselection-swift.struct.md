# LevelOfDetailComponent.LevelSelection

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

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
- [static let automatic: LevelOfDetailComponent.LevelSelection](./levelselection-swift.struct/automatic.md)
  Use automatic LOD selection based on the configured strategy.
### Type Methods
- [static func fixed(Int) -> LevelOfDetailComponent.LevelSelection](./levelselection-swift.struct/fixed%28_%29.md)
  Override automatic selection and always display the specified level index.

## See Also

### Choosing a level
- [var strategy: LevelOfDetailComponent.SelectionStrategy](./strategy.md)
- [LevelOfDetailComponent.SelectionStrategy](./selectionstrategy.md)
  The strategy used to select which detail level to display.
- [var levelSelection: LevelOfDetailComponent.LevelSelection](./levelselection-swift.property.md)
  The level selection mode. Defaults to automatic selection based on the strategy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/levelofdetailcomponent/levelselection-swift.struct)*