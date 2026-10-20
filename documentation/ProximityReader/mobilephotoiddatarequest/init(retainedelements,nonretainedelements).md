# init(retainedElements:nonRetainedElements:)

**Framework**: ProximityReader  
**Kind**: init  
**Role**: Initializer

Returns a photo ID data request.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
init(retainedElements: [MobilePhotoIDDataRequest.Element] = [], nonRetainedElements: [MobilePhotoIDDataRequest.Element] = [])
```

## See Also

### Creating a data request
- [MobilePhotoIDDataRequest.Element](./element.md)
  A type that represents an element you can request from a photo ID.
- [var nonRetainedElements: [MobilePhotoIDDataRequest.Element]](./nonretainedelements.md)
  The document elements you’re requesting and intend to retain no longer than necessary to process the result in realtime.
- [var retainedElements: [MobilePhotoIDDataRequest.Element]](./retainedelements.md)
  The document elements you’re requesting and intend to retain for an indefinite period of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobilephotoiddatarequest/init(retainedelements:nonretainedelements:))*