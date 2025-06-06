# CGPatternTiling.constantSpacing

**Framework**: Core Graphics  
**Kind**: case

Pattern cells are spaced consistently, as with [`CGPatternTiling.constantSpacingMinimalDistortion`](cgpatterntiling/constantspacingminimaldistortion.md).The pattern cell may be distorted additionally to permit a moreefficient implementation.

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
case constantSpacing
```

## See Also

- [CGPatternTiling.noDistortion](cgpatterntiling/nodistortion.md)
  The pattern cell is not distorted when painted.The spacing between pattern cells may vary by as much as 1 devicepixel.
- [CGPatternTiling.constantSpacingMinimalDistortion](cgpatterntiling/constantspacingminimaldistortion.md)
  Pattern cells are spaced consistently. Thepattern cell may be distorted by as much as 1 device pixel whenthe pattern is painted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpatterntiling/constantspacing)*