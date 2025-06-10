# showsContentTypes

**Framework**: AppKit  
**Kind**: property

`NSSavePanel`: Whether or not to show a control for selecting the type of the saved file. The control shows the types in `allowedContentTypes`. Default is `NO`. `NSOpenPanel`: Not used.

**Availability**:
- macOS 15.0+

## Declaration

```swift
@MainActor
var showsContentTypes: Bool { get set }
```

#### Discussion

> **Note**: If `allowedContentTypes` is empty, the control is not displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/showscontenttypes)*