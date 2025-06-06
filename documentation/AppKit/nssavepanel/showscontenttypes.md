# showsContentTypes

**Framework**: Appkit  
**Kind**: property

`NSSavePanel`: Whether or not to show a control for selecting the type of the saved file. The control shows the types in `allowedContentTypes`. Default is `NO`.

**Availability**:
- macOS 15.0+

## Declaration

```swift
@MainActor
var showsContentTypes: Bool { get set }
```

#### Discussion

> **Note**: If @c allowedContentTypes is empty, the control is not displayed. `NSOpenPanel`: Not used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppKit/nssavepanel/showscontenttypes)*