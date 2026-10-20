# AXCustomContentReturnBlock

**Framework**: Accessibility  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
typealias AXCustomContentReturnBlock = () -> [AXCustomContent]?
```

```c
typedef NSArray<AXCustomContent *> *(^)(void) AXCustomContentReturnBlock;
```

## See Also

### Custom accessibility content
- [class AXCustomContent](./axcustomcontent.md)
  Objects that define custom content and the timing of its output.
- [protocol AXCustomContentProvider](./axcustomcontentprovider.md)
  The interface for customizing the accessibility content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axcustomcontentreturnblock)*