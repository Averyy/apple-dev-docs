# init(identifier:)

**Framework**: AppKit  
**Kind**: init

Creates a newly allocated toolbar with the specified identifier.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
@MainActor
init(identifier: NSToolbar.Identifier)
```

#### Return Value

The initialized toolbar object.

#### Discussion

`identifier` is never seen by users and should not be localized. See the [`identifier`](nstoolbar/identifier-swift.property.md) property for important information.

## Parameters

- `identifier`: A string used by the class to identify the kind of the toolbar.

## See Also

- [var identifier: NSToolbar.Identifier](nstoolbar/identifier-swift.property.md)
  The value you use to identify the toolbar in your app.
- [Toolbar Programming Topics for Cocoa](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Toolbars/Toolbars.html#//apple_ref/doc/uid/10000109i)
- [convenience init()](nstoolbar/init.md)
  Creates a new toolbar with an empty identifier string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/init(identifier:))*