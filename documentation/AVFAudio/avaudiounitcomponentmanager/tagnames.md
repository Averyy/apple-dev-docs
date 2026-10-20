# tagNames

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

An array of all tags the audio unit associates with the current user, and the system tags the audio units define.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var tagNames: [String] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSString *> * tagNames;
```

## See Also

### Getting Audio Unit tags
- [var standardLocalizedTagNames: [String]](./standardlocalizedtagnames.md)
  An array of the localized standard system tags the audio units define.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitcomponentmanager/tagnames)*