# category

**Framework**: OSLog  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The payload’s category.

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
var category: String { get }
```

```objc
@property (nonatomic, readonly) NSString * category;
```

## Discussion

The category is derived from the `os_log_t` handle used.

## See Also

### Elements of a Payload
- [var components: [OSLogMessageComponent]](./components.md)
  The payload’s components.
- [var formatString: String](./formatstring.md)
  The payload’s format string.
- [var subsystem: String](./subsystem.md)
  The payload’s subsystem.


---

*[View on Apple Developer](https://developer.apple.com/documentation/oslog/oslogentrywithpayload/category)*