# init(retainedElements:nonRetainedElements:)

**Framework**: ProximityReader  
**Kind**: init  
**Role**: Initializer

Returns a photo ID raw data request.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
init(retainedElements: [MobilePhotoIDRawDataRequest.Element] = [], nonRetainedElements: [MobilePhotoIDRawDataRequest.Element] = [])
```

## See Also

### Creating a raw data request
- [MobilePhotoIDRawDataRequest.Element](./element.md)
  A type representing an element that you can request from a photo ID.
- [var nonRetainedElements: [MobilePhotoIDRawDataRequest.Element]](./nonretainedelements.md)
  The document elements you’re requesting and intend to retain no longer than is necessary to process the result in realtime.
- [var retainedElements: [MobilePhotoIDRawDataRequest.Element]](./retainedelements.md)
  The document elements you’re requesting and intend to retain for an indefinite period of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobilephotoidrawdatarequest/init(retainedelements:nonretainedelements:))*