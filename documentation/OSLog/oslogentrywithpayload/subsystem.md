# subsystem

**Framework**: OSLog  
**Kind**: property  
**Required**: Yes

The payload’s subsystem.

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
var subsystem: String { get }
```

#### Discussion

The category is derived from the `os_log_t` handle used.

## See Also

- [var category: String](oslogentrywithpayload/category.md)
  The payload’s category.
- [var components: [OSLogMessageComponent]](oslogentrywithpayload/components.md)
  The payload’s components.
- [var formatString: String](oslogentrywithpayload/formatstring.md)
  The payload’s format string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/oslog/oslogentrywithpayload/subsystem)*