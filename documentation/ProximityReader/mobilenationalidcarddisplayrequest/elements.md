# elements

**Framework**: Proximityreader  
**Kind**: property

The document elements you’re requesting.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
var elements: [MobileNationalIDCardDisplayRequest.Element]
```

#### Discussion

> **Note**: A request isn’t considered valid if the list of elements is empty, contains duplicates, or contains both [`age`](mobilenationalidcarddisplayrequest/element/age.md) and [`ageAtLeast(_:)`](mobilenationalidcarddisplayrequest/element/ageatleast(_:).md). If you call [`requestDocument(_:)`](mobiledocumentreadersession/requestdocument(_:).md) with an invalid request, the framework throws an [`MobileDocumentReaderError.invalidRequest`](mobiledocumentreadererror/invalidrequest.md) error.

## See Also

- [var region: Locale.Region](mobilenationalidcarddisplayrequest/region.md)
  The region of the document you’re requesting.
- [MobileNationalIDCardDisplayRequest.Element](mobilenationalidcarddisplayrequest/element.md)
  A type that represents an element you can request from a mobile national ID card.
- [var options: MobileNationalIDCardDisplayRequest.Options](mobilenationalidcarddisplayrequest/options-swift.property.md)
  An object that customizes how to perform a display request.
- [MobileNationalIDCardDisplayRequest.Options](mobilenationalidcarddisplayrequest/options-swift.struct.md)
  An object that customizes how to perform a display request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ProximityReader/mobilenationalidcarddisplayrequest/elements)*