# baseWritingDirection

**Framework**: AppKit  
**Kind**: property

The initial writing direction used to determine the actual writing direction for text.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var baseWritingDirection: NSWritingDirection { get set }
```

#### Discussion

The Text system uses this value as a hint for calculating the actual direction for displaying Unicode characters.  If no writing direction is set, returns `NSWritingDirectionNatural`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/basewritingdirection)*