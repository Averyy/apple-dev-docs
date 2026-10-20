# AXCustomContent.Importance

**Framework**: Accessibility  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum AXCustomContentImportance : NSUInteger;
```

## Topics

### Creating a content importance enumeration
- [init?(rawValue: UInt)](./importance-swift.enum/init%28rawvalue%29.md)
### Setting content importance
- [AXCustomContent.Importance.default](./importance-swift.enum/default.md)
  Output the content to the user on demand.
- [AXCustomContent.Importance.high](./importance-swift.enum/high.md)
  Output the content to the user immediately.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Defining custom content
- [var label: String](./label.md)
  A localized string that identifies the label for this content.
- [var attributedLabel: NSAttributedString](./attributedlabel.md)
  A localized attributed string that identifies the label for this content.
- [var value: String](./value.md)
  A localized string that provides a value for the label.
- [var attributedValue: NSAttributedString](./attributedvalue.md)
  A localized attributed string that provides a value for the label.
- [var importance: AXCustomContent.Importance](./importance-swift.property.md)
  An object that determines when to output custom accessibility content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axcustomcontent/importance-swift.enum)*