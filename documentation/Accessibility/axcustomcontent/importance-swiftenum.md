# AXCustomContent.Importance

**Framework**: Accessibility  
**Kind**: enum

Objects that control the timing of content output.

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
enum Importance
```

## Topics

### Creating a content importance enumeration
- [init?(rawValue: UInt)](axcustomcontent/importance-swift.enum/init(rawvalue:).md)
### Setting content importance
- [AXCustomContent.Importance.default](axcustomcontent/importance-swift.enum/default.md)
  Output the content to the user on demand.
- [AXCustomContent.Importance.high](axcustomcontent/importance-swift.enum/high.md)
  Output the content to the user immediately.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var label: String](axcustomcontent/label.md)
  A localized string that identifies the label for this content.
- [var attributedLabel: NSAttributedString](axcustomcontent/attributedlabel.md)
  A localized attributed string that identifies the label for this content.
- [var value: String](axcustomcontent/value.md)
  A localized string that provides a value for the label.
- [var attributedValue: NSAttributedString](axcustomcontent/attributedvalue.md)
  A localized attributed string that provides a value for the label.
- [var importance: AXCustomContent.Importance](axcustomcontent/importance-swift.property.md)
  An object that determines when to output custom accessibility content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axcustomcontent/importance-swift.enum)*