# identifier

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A string that identifies the custom intent object within your app.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var identifier: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, strong, readonly, nullable) NSString * identifier;
```

*macOS*

```objc
@property (atomic, strong, readonly, nullable) NSString * identifier;
```

## See Also

### Describing the Object for the System
- [var pronunciationHint: String?](./pronunciationhint.md)
  A hint that describes how to pronounce the custom intent object.
- [var alternativeSpeakableMatches: [INSpeakableString]?](./alternativespeakablematches.md)
  An array of alternative speakable strings that identify the object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inobject/identifier)*