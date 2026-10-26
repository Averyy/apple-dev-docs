# nonMonotonic

**Framework**: Core Text  
**Kind**: property  
**Role**: Type Property

The run isn’t in strictly increasing or decreasing order.

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
static var nonMonotonic: CTRunStatus { get }
```

```c
kCTRunStatusNonMonotonic
```

#### Discussion

The run is reordered so that the string indices associated with the glyphs aren’t in strictly increasing (for left-to-right runs) or decreasing (for right-to-left runs) order.

## See Also

### Constants
- [static var rightToLeft: CTRunStatus](./righttoleft.md)
  The run proceeds from right to left.
- [static var hasNonIdentityMatrix: CTRunStatus](./hasnonidentitymatrix.md)
  The run requires a specific text matrix to be set in the current Core Graphics context for proper drawing.
- [kCTRunStatusNoStatus](./kctrunstatusnostatus.md)
  The run has no special attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctrunstatus/nonmonotonic)*