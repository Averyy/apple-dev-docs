# autosaveName

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A unique name for saving and restoring information about a status item.

**Availability**:
- macOS 10.12+

## Declaration

```swift
var autosaveName: NSStatusItem.AutosaveName! { get set }
```

```objc
@property (copy, null_resettable) NSStatusItemAutosaveName autosaveName;
```

#### Discussion

If you do not provide an autosave name for a status item, the system automatically chooses a unique name. Setting this property to [`nil`](../../ObjectiveC/nil-227m0.md) resets it to the automatically chosen name.

Applications with multiple status items should set an autosave name after creating each item.

## See Also

### Setting the autosave name
- [NSStatusItem.AutosaveName](./autosavename-swift.typealias.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusitem/autosavename-swift.property)*