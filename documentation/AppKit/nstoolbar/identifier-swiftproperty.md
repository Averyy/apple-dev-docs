# identifier

**Framework**: AppKit  
**Kind**: property

The value you use to identify the toolbar in your app.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
@MainActor
var identifier: NSToolbar.Identifier { get }
```

#### Discussion

Use this property to distinguish toolbars in your app. Multiple toolbars can share the same identifier, and you might do so for windows that display similar content. When two or more toolbars share an identifier, they synchronize their state and display the same set of items.

If the toolbar autosaves its contents, the system associates the configuration data with this identifier.

## See Also

- [var autosavesConfiguration: Bool](nstoolbar/autosavesconfiguration.md)
  A Boolean value that indicates whether the toolbar autosaves its configuration.
- [NSToolbar.Identifier](nstoolbar/identifier-swift.typealias.md)
  A string value that you use to differentiate your app’s toolbars.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/identifier-swift.property)*