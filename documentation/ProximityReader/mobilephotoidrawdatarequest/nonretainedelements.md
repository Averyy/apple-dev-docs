# nonRetainedElements

**Framework**: ProximityReader  
**Kind**: property  
**Role**: Instance Property

The document elements you’re requesting and intend to retain no longer than is necessary to process the result in realtime.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var nonRetainedElements: [MobilePhotoIDRawDataRequest.Element]
```

## See Also

### Creating a raw data request
- [init(retainedElements: [MobilePhotoIDRawDataRequest.Element], nonRetainedElements: [MobilePhotoIDRawDataRequest.Element])](./init%28retainedelements,nonretainedelements%29.md)
  Returns a photo ID raw data request.
- [MobilePhotoIDRawDataRequest.Element](./element.md)
  A type representing an element that you can request from a photo ID.
- [var retainedElements: [MobilePhotoIDRawDataRequest.Element]](./retainedelements.md)
  The document elements you’re requesting and intend to retain for an indefinite period of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobilephotoidrawdatarequest/nonretainedelements)*