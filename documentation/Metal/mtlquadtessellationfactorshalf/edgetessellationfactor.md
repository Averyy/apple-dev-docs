# edgeTessellationFactor

**Framework**: Metal  
**Kind**: property

The edge tessellation factors, with each index value providing the tessellation factor for a particular edge.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var edgeTessellationFactor: (UInt16, UInt16, UInt16, UInt16)
```

#### Discussion

- The value in index 0 provides the tessellation factor for the left edge of the patch.
- The value in index 1 provides the tessellation factor for the top edge of the patch.
- The value in index 2 provides the tessellation factor for the right edge of the patch.
- The value in index 3 provides the tessellation factor for the bottom edge of the patch.

## See Also

- [var insideTessellationFactor: (UInt16, UInt16)](mtlquadtessellationfactorshalf/insidetessellationfactor.md)
  The inside tessellation factors, with the value in index 0 providing the horizontal tessellation factor and the value in index 1 providing the vertical tessellation factor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlquadtessellationfactorshalf/edgetessellationfactor)*