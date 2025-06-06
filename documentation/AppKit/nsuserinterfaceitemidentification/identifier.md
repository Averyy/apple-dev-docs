# identifier

**Framework**: AppKit  
**Kind**: property  
**Required**: Yes

A string that identifies the user interface item.

**Availability**:
- macOS ?+

## Declaration

```swift
var identifier: NSUserInterfaceItemIdentifier? { get set }
```

#### Discussion

Identifiers are used during window restoration operations to uniquely identify the windows of the application. You can set the value of this string programmatically or in Interface Builder. If you create an item in Interface Builder and do not set a value for this string, a unique value is created for the item when the nib file is loaded. For programmatically created views, you typically set this value after creating the item but before adding it to a window.

You should not change the value of a window’s identifier after adding any views to the window. For views and controls in a window, the value you specify for this string must be unique on a per-window basis.

The slash (`/`), backslash (`\`), or colon (`:`) characters are reserved and must not be used in your custom identifiers. Similarly, Apple reserves all identifiers beginning with an underscore (`_`) character. Applications and frameworks should use a consistent prefix for their identifiers to avoid collisions with other frameworks. For a list of prefixes used by the system frameworks, see [`OS X Frameworks`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/OSX_Technology_Overview/SystemFrameworks/SystemFrameworks.html#//apple_ref/doc/uid/TP40001067-CH210) in [`Mac Technology Overview`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/OSX_Technology_Overview/About/About.html#//apple_ref/doc/uid/TP40001067).

If you are subclassing a class from one of the system frameworks, do not override the accessor methods of this protocol.

## See Also

- [struct NSUserInterfaceItemIdentifier](nsuserinterfaceitemidentifier.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserinterfaceitemidentification/identifier)*