# showsContentTypes

**Framework**: AppKit  
**Kind**: property

Whether or not to show a popup list for selecting the type of the saved file.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var showsContentTypes: Bool { get set }
```

#### Discussion

The popup list shows the localized description for the types in `allowedContentTypes`. To display a different description, implement the delegate method `-panel:displayNameForType:`. The default value is `NO`, do not show the content types.

- Note: If `allowedContentTypes` is empty, the control is not displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/showscontenttypes)*