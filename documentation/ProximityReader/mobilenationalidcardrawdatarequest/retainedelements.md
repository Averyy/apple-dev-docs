# retainedElements

**Framework**: ProximityReader  
**Kind**: property  
**Role**: Instance Property

The document elements you’re requesting and intend to retain for an indefinite period of time.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
var retainedElements: [MobileNationalIDCardRawDataRequest.Element]
```

## See Also

### Configuring the request details
- [var region: Locale.Region](./region.md)
  The region of the document you’re requesting.
- [var nonRetainedElements: [MobileNationalIDCardRawDataRequest.Element]](./nonretainedelements.md)
  The document elements you’re requesting and intend to retain no longer than is necessary to process the result in realtime.
- [MobileNationalIDCardRawDataRequest.Element](./element.md)
  A type representing an element that you can request from a mobile national ID card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobilenationalidcardrawdatarequest/retainedelements)*