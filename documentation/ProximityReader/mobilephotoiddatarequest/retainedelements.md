# retainedElements

**Framework**: ProximityReader  
**Kind**: property  
**Role**: Instance Property

The document elements you’re requesting and intend to retain for an indefinite period of time.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var retainedElements: [MobilePhotoIDDataRequest.Element]
```

## See Also

### Creating a data request
- [init(retainedElements: [MobilePhotoIDDataRequest.Element], nonRetainedElements: [MobilePhotoIDDataRequest.Element])](./init%28retainedelements,nonretainedelements%29.md)
  Returns a photo ID data request.
- [MobilePhotoIDDataRequest.Element](./element.md)
  A type that represents an element you can request from a photo ID.
- [var nonRetainedElements: [MobilePhotoIDDataRequest.Element]](./nonretainedelements.md)
  The document elements you’re requesting and intend to retain no longer than necessary to process the result in realtime.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobilephotoiddatarequest/retainedelements)*