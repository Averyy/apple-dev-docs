# standardLocalizedTagNames

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

An array of the localized standard system tags the audio units define.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var standardLocalizedTagNames: [String] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSString *> * standardLocalizedTagNames;
```

## See Also

### Getting Audio Unit tags
- [var tagNames: [String]](./tagnames.md)
  An array of all tags the audio unit associates with the current user, and the system tags the audio units define.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitcomponentmanager/standardlocalizedtagnames)*