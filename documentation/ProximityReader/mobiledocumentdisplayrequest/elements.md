# elements

**Framework**: ProximityReader  
**Kind**: property

The document elements you’re requesting.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
var elements: [MobileDocumentDisplayRequest.Element]
```

#### Discussion

> **Note**: A request isn’t considered valid if the list of elements is empty, contains duplicates, or contains both [`age`](mobiledocumentdisplayrequest/element/age.md) and [`ageAtLeast(_:)`](mobiledocumentdisplayrequest/element/ageatleast(_:).md). If you call [`requestDocument(_:)`](mobiledocumentreadersession/requestdocument(_:).md) with an invalid request, the framework throws an [`MobileDocumentReaderError.invalidRequest`](mobiledocumentreadererror/invalidrequest.md) error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledocumentdisplayrequest/elements)*