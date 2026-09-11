# creationSource

**Framework**: SwiftUI  
**Kind**: property

The source associated with the button that created this document.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var creationSource: DocumentCreationSource? { get }
```

#### Discussion

On iOS, you can specify the source using a [`NewDocumentButton`](newdocumentbutton.md) in [`DocumentGroupLaunchScene`](documentgrouplaunchscene.md). On macOS, this is always `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentcreationcontext/creationsource)*