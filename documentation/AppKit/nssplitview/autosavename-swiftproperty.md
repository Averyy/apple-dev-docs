# autosaveName

**Framework**: AppKit  
**Kind**: property

The name to use when the system automatically saves the split view’s divider configuration.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var autosaveName: NSSplitView.AutosaveName? { get set }
```

#### Discussion

If this property’s value is `nil` or empty, autosaving doesn’t occur.

## See Also

- [NSSplitView.AutosaveName](nssplitview/autosavename-swift.typealias.md)
  The type that specifies the split view’s autosave name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitview/autosavename-swift.property)*