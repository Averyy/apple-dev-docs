# audioMessageFile

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

An audio recording that Siri plays to the message recipient.

**Availability**:
- iOS 16.0+ - Deprecated in 17.0
- iPadOS 16.0+ - Deprecated in 17.0
- Mac Catalyst 16.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.0+ - Deprecated in 10.0

> **Deprecated**: Use attachmentFile instead

## Declaration

```swift
@NSCopying
var audioMessageFile: INFile? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INFile * audioMessageFile;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INFile * audioMessageFile;
```

## See Also

### Getting the Content
- [var content: String?](./content.md)
  The text that Siri recites to the message recipient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmessage/audiomessagefile)*