# category

**Framework**: OSLog  
**Kind**: property  
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

#### Discussion

The category is derived from the `os_log_t` handle used.

## See Also

- [var components: [OSLogMessageComponent]](oslogentrywithpayload/components.md)
  The payload’s components.
- [var formatString: String](oslogentrywithpayload/formatstring.md)
  The payload’s format string.
- [var subsystem: String](oslogentrywithpayload/subsystem.md)
  The payload’s subsystem.


---

*[View on Apple Developer](https://developer.apple.com/documentation/oslog/oslogentrywithpayload/category)*