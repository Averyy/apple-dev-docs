# init(retainedElements:nonRetainedElements:)

**Framework**: ProximityReader  
**Kind**: init

Returns a photo ID data request.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(retainedElements: [MobilePhotoIDDataRequest.Element] = [], nonRetainedElements: [MobilePhotoIDDataRequest.Element] = [])
```

## See Also

- [MobilePhotoIDDataRequest.Element](mobilephotoiddatarequest/element.md)
  A type that represents an element you can request from a photo ID.
- [var nonRetainedElements: [MobilePhotoIDDataRequest.Element]](mobilephotoiddatarequest/nonretainedelements.md)
  The document elements you’re requesting and intend to retain no longer than necessary to process the result in realtime.
- [var retainedElements: [MobilePhotoIDDataRequest.Element]](mobilephotoiddatarequest/retainedelements.md)
  The document elements you’re requesting and intend to retain for an indefinite period of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobilephotoiddatarequest/init(retainedelements:nonretainedelements:))*