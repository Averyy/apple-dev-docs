# currentContentType

**Framework**: Appkit  
**Kind**: property

`NSSavePanel`:The current type. If set to `nil`, resets to the first allowed content type. Returns `nil` if `allowedContentTypes` is empty. `NSOpenPanel`: Not used.

**Availability**:
- macOS 15.0+

## Declaration

```swift
@MainActor
var currentContentType: UTType? { get set }
```

#### Discussion

> **Note**: Asserts that `currentContentType` conforms to `UTTypeData` or `UTTypeDirectory`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppKit/nssavepanel/currentcontenttype)*