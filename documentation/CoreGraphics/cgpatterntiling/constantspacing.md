# CGPatternTiling.constantSpacing

**Framework**: Core Graphics  
**Kind**: case  
**Role**: Case

Pattern cells are spaced consistently, as with [`CGPatternTiling.constantSpacingMinimalDistortion`](./constantspacingminimaldistortion.md).The pattern cell may be distorted additionally to permit a moreefficient implementation.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
case constantSpacing
```

```c
kCGPatternTilingConstantSpacing
```

## See Also

### Constants
- [CGPatternTiling.noDistortion](./nodistortion.md)
  The pattern cell is not distorted when painted.The spacing between pattern cells may vary by as much as 1 devicepixel.
- [CGPatternTiling.constantSpacingMinimalDistortion](./constantspacingminimaldistortion.md)
  Pattern cells are spaced consistently. Thepattern cell may be distorted by as much as 1 device pixel whenthe pattern is painted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpatterntiling/constantspacing)*