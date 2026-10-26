# alternativeSpeakableMatches

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

An array of alternative phrases that match the current phrase.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var alternativeSpeakableMatches: [any INSpeakable]? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, strong, readonly, nullable) NSArray<id<INSpeakable>> * alternativeSpeakableMatches;
```

*macOS*

```objc
@property (atomic, strong, readonly, nullable) NSArray<id<INSpeakable>> * alternativeSpeakableMatches;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inspeakable/alternativespeakablematches)*