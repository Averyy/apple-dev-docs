# DocumentBaseBox

**Framework**: SwiftUI  
**Kind**: protocol

A Box that allows setting its Document base not requiring the caller to know the exact types of the box and its base.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
protocol DocumentBaseBox<Document> : AnyObject
```

## Topics

### Associated Types
- [associatedtype Document](documentbasebox/document.md)
  The underlying document type.
### Instance Properties
- [var base: Self.Document?](documentbasebox/base.md)
  Updates the underlying document to a new value.

## See Also

- [struct DocumentGroupLaunchScene](documentgrouplaunchscene.md)
  A launch scene for document-based applications.
- [struct DocumentLaunchView](documentlaunchview.md)
  A view to present when launching document-related user experience.
- [struct DocumentLaunchGeometryProxy](documentlaunchgeometryproxy.md)
  A proxy for access to the frame of the scene and its title view.
- [struct DefaultDocumentGroupLaunchActions](defaultdocumentgrouplaunchactions.md)
  The default actions for the document group launch scene and the document launch view.
- [struct NewDocumentButton](newdocumentbutton.md)
  A button that creates and opens new documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentbasebox)*