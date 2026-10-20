# region

**Framework**: ProximityReader  
**Kind**: property  
**Role**: Instance Property

The region of the document you’re requesting.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
var region: Locale.Region
```

## See Also

### Configuring the request details
- [var retainedElements: [MobileNationalIDCardDataRequest.Element]](./retainedelements.md)
  The document elements you’re requesting and intend to retain for an indefinite period of time.
- [var nonRetainedElements: [MobileNationalIDCardDataRequest.Element]](./nonretainedelements.md)
  The document elements you’re requesting and intend to retain no longer than necessary to process the result in realtime.
- [MobileNationalIDCardDataRequest.Element](./element.md)
  A type that represents an element you can request from a mobile national ID card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobilenationalidcarddatarequest/region)*