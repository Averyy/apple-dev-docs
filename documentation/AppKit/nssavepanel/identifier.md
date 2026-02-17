# identifier

**Framework**: AppKit  
**Kind**: property

Sets and returns the identifier.

**Availability**:
- macOS ?+

## Declaration

```swift
var identifier: NSUserInterfaceItemIdentifier? { get set }
```

#### Discussion

The panel’s current state such as the root directory and the current directory are saved and restored relative to the identifier.

> **Note**: When the identifier is changed, the properties that depend on the identifier are updated from user defaults. Properties that have a null value in user defaults are not changed (and keep their existing value).

> **Note**: Can only be set during the configuration phase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/identifier)*