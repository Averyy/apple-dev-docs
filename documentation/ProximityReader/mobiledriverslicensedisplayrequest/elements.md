# elements

**Framework**: ProximityReader  
**Kind**: property

The document elements you’re requesting.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
var elements: [MobileDriversLicenseDisplayRequest.Element]
```

#### Discussion

> **Note**: A request isn’t considered valid if the list of elements is empty, contains duplicates, or contains both [`age`](mobiledriverslicensedisplayrequest/element/age.md) and [`ageAtLeast(_:)`](mobiledriverslicensedisplayrequest/element/ageatleast(_:).md). If you call [`requestDocument(_:)`](mobiledocumentreadersession/requestdocument(_:).md) with an invalid request, the framework throws an [`MobileDocumentReaderError.invalidRequest`](mobiledocumentreadererror/invalidrequest.md) error.

## See Also

- [init(elements: [MobileDriversLicenseDisplayRequest.Element], options: MobileDriversLicenseDisplayRequest.Options)](mobiledriverslicensedisplayrequest/init(elements:options:).md)
  Creates a new mobile driver’s license display request.
- [MobileDriversLicenseDisplayRequest.Element](mobiledriverslicensedisplayrequest/element.md)
  A type that represents an element you can request from a mobile driver’s license.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledriverslicensedisplayrequest/elements)*