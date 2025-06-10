# principalMediaCharacteristics

**Framework**: AVFoundation  
**Kind**: property

An array of media characteristics that are essential to select when choosing media with a particular characteristic.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var principalMediaCharacteristics: [AVMediaCharacteristic]? { get }
```

#### Discussion

If no option matches the principal media characteristics, the system chooses the default option in the group as the best match.

When making automatic selections, a player item treats principal media characteristics as criteria that supersede language preferences and preferred media characteristics.

> ❗ **Important**:  Use principal media characteristics with caution. It’s typical to support accessibility features using a combination of language preferences and preferred characteristics, and not using principal media characteristics.

## See Also

- [var preferredLanguages: [String]?](avplayermediaselectioncriteria/preferredlanguages.md)
  An array of language identifiers in preferred order.
- [var preferredMediaCharacteristics: [AVMediaCharacteristic]?](avplayermediaselectioncriteria/preferredmediacharacteristics.md)
  An array of media characteristics in preferred order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayermediaselectioncriteria/principalmediacharacteristics)*