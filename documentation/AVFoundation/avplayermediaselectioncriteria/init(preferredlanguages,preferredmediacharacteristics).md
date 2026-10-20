# init(preferredLanguages:preferredMediaCharacteristics:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates media selection criteria with the preferred languages and media characteristics.

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
init(preferredLanguages: [String]?, preferredMediaCharacteristics: [AVMediaCharacteristic]?)
```

```objc
- (instancetype) initWithPreferredLanguages:(NSArray<NSString *> *) preferredLanguages preferredMediaCharacteristics:(NSArray<NSString *> *) preferredMediaCharacteristics;
```

## Parameters

- `preferredLanguages`: An array of language identifier strings, in order of preference. This value may be `nil`.
- `preferredMediaCharacteristics`: An array of media characteristics, in order of preference. This value may be `nil`.

## See Also

### Creating media selection criteria
- [init(principalMediaCharacteristics: [AVMediaCharacteristic]?, preferredLanguages: [String]?, preferredMediaCharacteristics: [AVMediaCharacteristic]?)](./init%28principalmediacharacteristics,preferredlanguages,preferredmediacharacteristics%29.md)
  Creates media selection criteria with the principal media characteristics, and preferred languages and media characteristics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayermediaselectioncriteria/init(preferredlanguages:preferredmediacharacteristics:))*