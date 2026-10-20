# allowedMenuBarItems

**Framework**: Automatic Assessment Configuration  
**Kind**: property  
**Role**: Instance Property

The set of menu bar items that should remain visible during an assessment.

**Availability**:
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
var allowedMenuBarItems: Set<AEMenuBarItem>? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSSet<NSString *> * allowedMenuBarItems;
```

#### Discussion

When [`allowsMenuBar`](./allowsmenubar.md) is `true`, the menu bar is restricted to only the items specified in this set. If this property is `nil`, all menu bar items are allowed (unrestricted menu bar).

> **Note**: This property only takes effect when [`allowsMenuBar`](./allowsmenubar.md) is `true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowedmenubaritems)*