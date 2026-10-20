# unifiedCompact

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A window toolbar style similar to [`unified`](./unified.md), but with a more compact vertical sizing.

**Availability**:
- macOS 11.0+

## Declaration

```swift
@export(implementation)
static var unifiedCompact: UnifiedCompactWindowToolbarStyle { get }
```

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

## See Also

### Getting built-in window toolbar styles
- [static var automatic: DefaultWindowToolbarStyle](./automatic.md)
  The automatic window toolbar style.
- [static var expanded: ExpandedWindowToolbarStyle](./expanded.md)
  A window toolbar style which displays its title bar area above the toolbar.
- [static var unified: UnifiedWindowToolbarStyle](./unified.md)
  A window toolbar style which displays its toolbar and title bar inline.
- [static func unified(showsTitle: Bool) -> UnifiedWindowToolbarStyle](./unified%28showstitle%29.md)
  A window toolbar style which displays its toolbar and title bar inline.
- [static func unifiedCompact(showsTitle: Bool) -> UnifiedCompactWindowToolbarStyle](./unifiedcompact%28showstitle%29.md)
  A window toolbar style similar to [`unified`](./unified.md), but with a more compact vertical sizing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowtoolbarstyle/unifiedcompact)*