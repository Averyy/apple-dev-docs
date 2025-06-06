# AXCustomContentProvider

**Framework**: Accessibility  
**Kind**: protocol

The interface for customizing the accessibility content.

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
protocol AXCustomContentProvider : NSObjectProtocol
```

## Topics

### Providing custom content
- [var accessibilityCustomContent: [AXCustomContent]!](axcustomcontentprovider/accessibilitycustomcontent.md)
  An array of custom objects for creating accessible content.
### Instance Properties
- [var accessibilityCustomContentBlock: AXCustomContentReturnBlock?](axcustomcontentprovider/accessibilitycustomcontentblock.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AXCustomContent](axcustomcontent.md)
  Objects that define custom content and the timing of its output.
- [typealias AXCustomContentReturnBlock](axcustomcontentreturnblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axcustomcontentprovider)*