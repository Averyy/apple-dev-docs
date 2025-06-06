# configuration

**Framework**: AppKit  
**Kind**: property

A dictionary containing the current configuration details for the toolbar.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
var configuration: [String : Any] { get }
```

#### Discussion

Use this property to retrieve the toolbar’s configuration details so you can save them to disk yourself. The dictionary in this property contains the identifiers of the current toolbar items and the values of important properties such as [`displayMode`](nstoolbar/displaymode-swift.property.md) and [`isVisible`](nstoolbar/isvisible.md).

## See Also

- [var autosavesConfiguration: Bool](nstoolbar/autosavesconfiguration.md)
  A Boolean value that indicates whether the toolbar autosaves its configuration.
- [func setConfiguration([String : Any])](nstoolbar/setconfiguration(_:).md)
  Specifies the new configuration details for the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/configuration)*