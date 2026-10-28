# spokenPhrase

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The phrase identified by Siri.

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
var spokenPhrase: String { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, strong, readonly, nonnull) NSString * spokenPhrase;
```

*macOS*

```objc
@property (atomic, strong, readonly, nonnull) NSString * spokenPhrase;
```

## Mentions

- [Handling an Intent](../../SiriKit/handling-an-intent.md)

## Discussion

Typically, this phrase corresponds to a custom term defined in the `AppIntentVocabulary.plist` file of your Intents extension, but it may also be a custom phrase spoken by the user. In both cases, it represents a term that you must resolve as part of handling an intent. For example, it might contain a workout name that you must resolve.

## See Also

### Getting the Spoken Attributes
- [var pronunciationHint: String?](./pronunciationhint.md)
  A hint at how the spoken phrase is pronounced.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inspeakable/spokenphrase)*