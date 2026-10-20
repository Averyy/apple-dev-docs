# supportsMultichannelContent

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether your app supplies multichannel audio content.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var supportsMultichannelContent: Bool { get }
```

```objc
@property (readonly) BOOL supportsMultichannelContent;
```

#### Discussion

The default value is `false`.

## See Also

### Configuring multichannel support
- [func setSupportsMultichannelContent(Bool) throws](./setsupportsmultichannelcontent%28_%29.md)
  Sets whether your app supplies multichannel audio content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/supportsmultichannelcontent)*