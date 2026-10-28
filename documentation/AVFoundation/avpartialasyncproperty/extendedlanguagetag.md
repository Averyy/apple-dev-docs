# extendedLanguageTag

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

The language tag of the track.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var extendedLanguageTag: AVAsyncProperty<Root, String?> { get }
```

Available when `Root` inherits `AVAssetTrack`.

## Discussion

Use the [`load(_:isolation:)`](../avasynchronouskeyvalueloading/load%28_,isolation%29.md) method to retrieve the property value.

The value is a [BCP-47](https://tools.ietf.org/html/bcp47) language tag, or `nil` if the track doesn’t specify a language tag.

## See Also

### Loading language support
- [static var languageCode: AVAsyncProperty<Root, String?>](./languagecode.md)
  The language code of the track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/extendedlanguagetag)*