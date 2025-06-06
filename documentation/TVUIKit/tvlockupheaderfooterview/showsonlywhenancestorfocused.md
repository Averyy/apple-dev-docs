# showsOnlyWhenAncestorFocused

**Framework**: TVUIKit  
**Kind**: property

A Boolean value indicating whether titles and subtitles are displayed when a lockup view isn’t in focus.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
@MainActor
var showsOnlyWhenAncestorFocused: Bool { get set }
```

#### Discussion

Set this value to `FALSE` to display header and footer information while the lockup view is not in focus. Header and footer information is always shown when a lockup view is in focus, regardless of this property’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvlockupheaderfooterview/showsonlywhenancestorfocused)*