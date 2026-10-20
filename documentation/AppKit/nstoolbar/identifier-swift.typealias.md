# NSToolbar.Identifier

**Framework**: AppKit  
**Kind**: typealias  
**Role**: Type Alias

A string value that you use to differentiate your app’s toolbars.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS

## Declaration

```swift
typealias Identifier = String
```

```c
typedef NSString * NSToolbarIdentifier;
```

#### Discussion

Multiple toolbar objects can have the same identifier. If two or more toolbars share an identifier, the system synchronizes the state of the toolbars and displays the same items for each one.

## See Also

### Getting the toolbar’s identity
- [var identifier: NSToolbar.Identifier](./identifier-swift.property.md)
  The value you use to identify the toolbar in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/identifier-swift.typealias)*