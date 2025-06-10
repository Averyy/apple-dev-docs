# init(retainedElements:nonRetainedElements:)

**Framework**: ProximityReader  
**Kind**: init

Returns a mobile driver’s license raw data request.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(retainedElements: [MobilePhotoIDRawDataRequest.Element] = [], nonRetainedElements: [MobilePhotoIDRawDataRequest.Element] = [])
```

## See Also

- [MobilePhotoIDRawDataRequest.Element](mobilephotoidrawdatarequest/element.md)
  A type representing an element that you can request from a photo ID.
- [var nonRetainedElements: [MobilePhotoIDRawDataRequest.Element]](mobilephotoidrawdatarequest/nonretainedelements.md)
  The document elements you’re requesting and intend to retain no longer than is necessary to process the result in realtime.
- [var retainedElements: [MobilePhotoIDRawDataRequest.Element]](mobilephotoidrawdatarequest/retainedelements.md)
  The document elements you’re requesting and intend to retain for an indefinite period of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobilephotoidrawdatarequest/init(retainedelements:nonretainedelements:))*