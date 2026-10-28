# init(principalMediaCharacteristics:preferredLanguages:preferredMediaCharacteristics:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates media selection criteria with the principal media characteristics, and preferred languages and media characteristics.

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
init(principalMediaCharacteristics: [AVMediaCharacteristic]?, preferredLanguages: [String]?, preferredMediaCharacteristics: [AVMediaCharacteristic]?)
```

```objc
- (instancetype) initWithPrincipalMediaCharacteristics:(NSArray<NSString *> *) principalMediaCharacteristics preferredLanguages:(NSArray<NSString *> *) preferredLanguages preferredMediaCharacteristics:(NSArray<NSString *> *) preferredMediaCharacteristics;
```

## Discussion

Principal media characteristics, when present, override language preferences when making selections within a specific media selection group. However, language preferences may still pertain to selections in other groups. For example, the system may consider language preferences when choosing whether to select nonforced subtitles for translation purposes.

## Parameters

- `principalMediaCharacteristics`: An array of media characteristics that are essential to selecting media with the characteristic. This value may be `nil`.
- `preferredLanguages`: An array of language identifier strings, in order of preference. This value may be `nil`.
- `preferredMediaCharacteristics`: An array of media characteristics, in order of preference. This value may be `nil`.

## See Also

### Creating media selection criteria
- [init(preferredLanguages: [String]?, preferredMediaCharacteristics: [AVMediaCharacteristic]?)](./init%28preferredlanguages,preferredmediacharacteristics%29.md)
  Creates media selection criteria with the preferred languages and media characteristics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayermediaselectioncriteria/init(principalmediacharacteristics:preferredlanguages:preferredmediacharacteristics:))*