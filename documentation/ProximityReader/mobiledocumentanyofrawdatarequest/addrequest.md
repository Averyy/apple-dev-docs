# addRequest(_:)

**Framework**: ProximityReader  
**Kind**: method

Adds the request as a candidate of this composite request.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
mutating func addRequest(_ request: any MobileDocumentRawDataRequest)
```

#### Discussion

> **Note**: A request isn’t considered valid if it contains requests that are not raw data requests. If you call [`requestDocument(_:)`](mobiledocumentreadersession/requestdocument(_:).md) with an invalid request, the framework throws a [`MobileDocumentReaderError.invalidRequest`](mobiledocumentreadererror/invalidrequest.md) error.

## Parameters

- `request`: The child request.

## See Also

- [init()](mobiledocumentanyofrawdatarequest/init.md)
  Returns a composite mobile document raw data request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledocumentanyofrawdatarequest/addrequest(_:))*