# preferredLanguages

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An array of language identifiers in preferred order.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var preferredLanguages: [String]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSArray<NSString *> * preferredLanguages;
```

## See Also

### Retrieving selection criteria settings
- [var preferredMediaCharacteristics: [AVMediaCharacteristic]?](./preferredmediacharacteristics.md)
  An array of media characteristics in preferred order.
- [var principalMediaCharacteristics: [AVMediaCharacteristic]?](./principalmediacharacteristics.md)
  An array of media characteristics that are essential to select when choosing media with a particular characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayermediaselectioncriteria/preferredlanguages)*