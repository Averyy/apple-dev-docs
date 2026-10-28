# pronunciationHint

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A hint that describes how to pronounce the custom intent object.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var pronunciationHint: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, strong, readonly, nullable) NSString * pronunciationHint;
```

*macOS*

```objc
@property (atomic, strong, readonly, nullable) NSString * pronunciationHint;
```

## Discussion

This property provides a soundalike equivalent of the object’s [`displayString`](./displaystring.md) to Siri, rather than a phonetic spelling. For example, the phrase “iTunes” might have “eye toons” as its pronunciation string.

## See Also

### Describing the Object for the System
- [var identifier: String?](./identifier.md)
  A string that identifies the custom intent object within your app.
- [var alternativeSpeakableMatches: [INSpeakableString]?](./alternativespeakablematches.md)
  An array of alternative speakable strings that identify the object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inobject/pronunciationhint)*