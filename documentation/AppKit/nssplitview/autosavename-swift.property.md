# autosaveName

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The name to use when the system automatically saves the split view’s divider configuration.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var autosaveName: NSSplitView.AutosaveName? { get set }
```

```objc
@property (copy, nullable) NSSplitViewAutosaveName autosaveName;
```

## Discussion

If this property’s value is `nil` or empty, autosaving doesn’t occur.

## See Also

### Saving Subview Positions
- [NSSplitView.AutosaveName](./autosavename-swift.typealias.md)
  The type that specifies the split view’s autosave name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitview/autosavename-swift.property)*