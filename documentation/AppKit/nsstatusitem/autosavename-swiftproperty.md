# autosaveName

**Framework**: AppKit  
**Kind**: property

A unique name for saving and restoring information about a status item.

**Availability**:
- macOS 10.12+

## Declaration

```swift
var autosaveName: NSStatusItem.AutosaveName! { get set }
```

#### Discussion

If you do not provide an autosave name for a status item, the system automatically chooses a unique name. Setting this property to [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0) resets it to the automatically chosen name.

Applications with multiple status items should set an autosave name after creating each item.

## See Also

- [NSStatusItem.AutosaveName](nsstatusitem/autosavename-swift.typealias.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusitem/autosavename-swift.property)*