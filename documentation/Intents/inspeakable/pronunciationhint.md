# pronunciationHint

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A hint at how the spoken phrase is pronounced.

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

#### Discussion

This value provides a hint to Siri about how a string is pronounced. This string is not a phonetic spelling of the original phrase, but is a string that has an equivalent sound when spoken. For example, the phrase “iTunes” could be have “eye toons” as its pronunciation string.

## See Also

### Getting the Spoken Attributes
- [var spokenPhrase: String](./spokenphrase.md)
  The phrase identified by Siri.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inspeakable/pronunciationhint)*