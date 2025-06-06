# itemIdentifiers

**Framework**: AppKit  
**Kind**: property

An array of itemIdentifiers that represent the current items in the toolbar. Setting this property will set the current items in the toolbar by diffing against items that already exist. Use this with great caution if `allowsUserCustomization` is enabled as it will override any customizations the user has made. This property is key value observable.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
@MainActor
var itemIdentifiers: [NSToolbarItem.Identifier] { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/itemidentifiers)*