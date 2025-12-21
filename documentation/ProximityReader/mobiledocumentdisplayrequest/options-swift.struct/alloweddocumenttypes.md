# allowedDocumentTypes

**Framework**: ProximityReader  
**Kind**: property

The allowed document types of the mobile document request.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
var allowedDocumentTypes: [MobileDocumentDisplayRequest.Options.DocumentType]
```

#### Discussion

> **Note**: A request isn’t considered valid if the list of allowed document types is empty or contains duplicates. If you call [`requestDocument(_:)`](mobiledocumentreadersession/requestdocument(_:).md) with an invalid request, the framework throws an [`MobileDocumentReaderError.invalidRequest`](mobiledocumentreadererror/invalidrequest.md) error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledocumentdisplayrequest/options-swift.struct/alloweddocumenttypes)*