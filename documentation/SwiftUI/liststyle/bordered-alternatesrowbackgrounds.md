# bordered(alternatesRowBackgrounds:)

**Framework**: SwiftUI  
**Kind**: method

The list style that describes the behavior and appearance of a list with standard border.

**Availability**:
- macOS 12.0+

## Declaration

```swift
static func bordered(alternatesRowBackgrounds: Bool) -> BorderedListStyle
```

#### Discussion

Bordered lists are expected to be inset from their outer containers, but do not have inset style rows or selection.

## Parameters

- `alternatesRowBackgrounds`: Whether the rows should alternate   their backgrounds to help visually distinguish them from each other.

## See Also

- [static func inset(alternatesRowBackgrounds: Bool) -> InsetListStyle](liststyle/inset(alternatesrowbackgrounds:).md)
  The list style that describes the behavior and appearance of an inset list with optional alternating row backgrounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/liststyle/bordered(alternatesrowbackgrounds:))*