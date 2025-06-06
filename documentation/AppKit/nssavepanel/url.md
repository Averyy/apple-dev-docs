# url

**Framework**: AppKit  
**Kind**: property

A URL that contains the fully specified location of the targeted file.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var url: URL? { get }
```

#### Discussion

The [`NSOpenPanel`](nsopenpanel.md) subclass sets this property to `nil` when the selection contains multiple items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/url)*