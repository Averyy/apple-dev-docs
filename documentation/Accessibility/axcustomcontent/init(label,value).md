# init(label:value:)

**Framework**: Accessibility  
**Kind**: init  
**Role**: Initializer

Creates new custom content with a label and value.

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
convenience init(label: String, value: String)
```

```objc
+ (instancetype) customContentWithLabel:(NSString *) label value:(NSString *) value;
```

## Parameters

- `label`: A localized string that identifies the label for this content.
- `value`: A localized string that provides a value for the label.

## See Also

### Creating custom content
- [convenience init(attributedLabel: NSAttributedString, attributedValue: NSAttributedString)](./init%28attributedlabel,attributedvalue%29.md)
  Creates new custom content with an attributed string and attributed value.
- [init?(coder: NSCoder)](./init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axcustomcontent/init(label:value:))*