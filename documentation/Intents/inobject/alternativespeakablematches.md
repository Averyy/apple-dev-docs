# alternativeSpeakableMatches

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

An array of alternative speakable strings that identify the object.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var alternativeSpeakableMatches: [INSpeakableString]? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, strong, readwrite, nullable) NSArray<INSpeakableString *> * alternativeSpeakableMatches;
```

*macOS*

```objc
@property (atomic, strong, readwrite, nullable) NSArray<INSpeakableString *> * alternativeSpeakableMatches;
```

## See Also

### Describing the Object for the System
- [var identifier: String?](./identifier.md)
  A string that identifies the custom intent object within your app.
- [var pronunciationHint: String?](./pronunciationhint.md)
  A hint that describes how to pronounce the custom intent object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inobject/alternativespeakablematches)*