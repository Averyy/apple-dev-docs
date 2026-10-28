# components

**Framework**: OSLog  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The payload’s components.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var components: [OSLogMessageComponent] { get }
```

```objc
@property (nonatomic, readonly) NSArray<OSLogMessageComponent *> * components;
```

## Discussion

This property contains an array of [`OSLogMessageComponent`](../oslogmessagecomponent.md) objects from the composed message.

## See Also

### Elements of a Payload
- [var category: String](./category.md)
  The payload’s category.
- [var formatString: String](./formatstring.md)
  The payload’s format string.
- [var subsystem: String](./subsystem.md)
  The payload’s subsystem.


---

*[View on Apple Developer](https://developer.apple.com/documentation/oslog/oslogentrywithpayload/components)*