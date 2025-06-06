# allowsDisplayModeCustomization

**Framework**: AppKit  
**Kind**: property

Whether or not the user is allowed to change display modes at run time. This functionality is independent of customizing the order of the items themselves. Only disable when the functionality or legibility of your toolbar could not be improved by another display mode. The user’s selection will be persisted using the toolbar’s `identifier` when `autosavesConfiguration` is enabled. The default is YES for apps linked on macOS 15.0 and above.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
@MainActor
var allowsDisplayModeCustomization: Bool { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/allowsdisplaymodecustomization)*