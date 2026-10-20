# init(attributedLabel:attributedValue:)

**Framework**: Accessibility  
**Kind**: init  
**Role**: Initializer

Creates new custom content with an attributed string and attributed value.

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
convenience init(attributedLabel label: NSAttributedString, attributedValue value: NSAttributedString)
```

```objc
+ (instancetype) customContentWithAttributedLabel:(NSAttributedString *) label attributedValue:(NSAttributedString *) value;
```

## Parameters

- `label`: A localized attributed string that identifies the label for this content.
- `value`: A localized attributed string that provides a value for the label.

## See Also

### Creating custom content
- [convenience init(label: String, value: String)](./init%28label,value%29.md)
  Creates new custom content with a label and value.
- [init?(coder: NSCoder)](./init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axcustomcontent/init(attributedlabel:attributedvalue:))*