# attributedLabel

**Framework**: Accessibility  
**Kind**: property  
**Role**: Instance Property

A localized attributed string that identifies the label for this content.

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
@NSCopying
var attributedLabel: NSAttributedString { get }
```

```objc
@property (nonatomic, copy, readonly) NSAttributedString * attributedLabel;
```

## See Also

### Defining custom content
- [var label: String](./label.md)
  A localized string that identifies the label for this content.
- [var value: String](./value.md)
  A localized string that provides a value for the label.
- [var attributedValue: NSAttributedString](./attributedvalue.md)
  A localized attributed string that provides a value for the label.
- [var importance: AXCustomContent.Importance](./importance-swift.property.md)
  An object that determines when to output custom accessibility content.
- [AXCustomContent.Importance](./importance-swift.enum.md)
  Objects that control the timing of content output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axcustomcontent/attributedlabel)*