# elements

**Framework**: ProximityReader  
**Kind**: property  
**Role**: Instance Property

The document elements you’re requesting.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
var elements: [MobileNationalIDCardDisplayRequest.Element]
```

#### Discussion

> **Note**: A request isn’t considered valid if the list of elements is empty, contains duplicates, or contains both [`age`](./element/age.md) and [`ageAtLeast(_:)`](./element/ageatleast%28_%29.md). If you call [`requestDocument(_:)`](../mobiledocumentreadersession/requestdocument%28_%29.md) with an invalid request, the framework throws an [`MobileDocumentReaderError.invalidRequest`](../mobiledocumentreadererror/invalidrequest.md) error.

## See Also

### Configuring the request details
- [var region: Locale.Region](./region.md)
  The region of the document you’re requesting.
- [MobileNationalIDCardDisplayRequest.Element](./element.md)
  A type that represents an element you can request from a mobile national ID card.
- [var options: MobileNationalIDCardDisplayRequest.Options](./options-swift.property.md)
  An object that customizes how to perform a display request.
- [MobileNationalIDCardDisplayRequest.Options](./options-swift.struct.md)
  An object that customizes how to perform a display request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobilenationalidcarddisplayrequest/elements)*