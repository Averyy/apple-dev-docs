# CGPatternTiling.noDistortion

**Framework**: Core Graphics  
**Kind**: case

The pattern cell is not distorted when painted.The spacing between pattern cells may vary by as much as 1 devicepixel.

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
case noDistortion
```

## See Also

- [CGPatternTiling.constantSpacingMinimalDistortion](cgpatterntiling/constantspacingminimaldistortion.md)
  Pattern cells are spaced consistently. Thepattern cell may be distorted by as much as 1 device pixel whenthe pattern is painted.
- [CGPatternTiling.constantSpacing](cgpatterntiling/constantspacing.md)
  Pattern cells are spaced consistently, as with [`CGPatternTiling.constantSpacingMinimalDistortion`](cgpatterntiling/constantspacingminimaldistortion.md).The pattern cell may be distorted additionally to permit a moreefficient implementation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpatterntiling/nodistortion)*