# content

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The text that Siri recites to the message recipient.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var content: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * content;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * content;
```

## See Also

### Getting the Content
- [var audioMessageFile: INFile?](./audiomessagefile.md)
  An audio recording that Siri plays to the message recipient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmessage/content)*