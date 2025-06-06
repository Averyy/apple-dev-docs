# nonMonotonic

**Framework**: Core Text  
**Kind**: property

The run isn’t in strictly increasing or decreasing order.

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
static var nonMonotonic: CTRunStatus { get }
```

#### Discussion

The run is reordered so that the string indices associated with the glyphs aren’t in strictly increasing (for left-to-right runs) or decreasing (for right-to-left runs) order.

## See Also

- [static var rightToLeft: CTRunStatus](ctrunstatus/righttoleft.md)
  The run proceeds from right to left.
- [static var hasNonIdentityMatrix: CTRunStatus](ctrunstatus/hasnonidentitymatrix.md)
  The run requires a specific text matrix to be set in the current Core Graphics context for proper drawing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctrunstatus/nonmonotonic)*