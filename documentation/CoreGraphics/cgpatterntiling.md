# CGPatternTiling

**Framework**: Core Graphics  
**Kind**: enum

Different methods for rendering a tiled pattern.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum CGPatternTiling
```

## Topics

### Constants
- [CGPatternTiling.noDistortion](cgpatterntiling/nodistortion.md)
  The pattern cell is not distorted when painted.The spacing between pattern cells may vary by as much as 1 devicepixel.
- [CGPatternTiling.constantSpacingMinimalDistortion](cgpatterntiling/constantspacingminimaldistortion.md)
  Pattern cells are spaced consistently. Thepattern cell may be distorted by as much as 1 device pixel whenthe pattern is painted.
- [CGPatternTiling.constantSpacing](cgpatterntiling/constantspacing.md)
  Pattern cells are spaced consistently, as with [`CGPatternTiling.constantSpacingMinimalDistortion`](cgpatterntiling/constantspacingminimaldistortion.md).The pattern cell may be distorted additionally to permit a moreefficient implementation.
### Initializers
- [init?(rawValue: Int32)](cgpatterntiling/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpatterntiling)*