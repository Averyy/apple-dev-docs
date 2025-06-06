# AXCustomContent

**Framework**: Accessibility  
**Kind**: class

Objects that define custom content and the timing of its output.

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
class AXCustomContent
```

#### Overview

An `AXCustomContent` object contains the accessibility strings for the labels you apply to your accessibility content. Combine them with the [`AXCustomContentProvider`](axcustomcontentprovider.md) protocol to allow your users to experience the content in a more appropriate manner for each assistive technology.

## Topics

### Creating custom content
- [convenience init(attributedLabel: NSAttributedString, attributedValue: NSAttributedString)](axcustomcontent/init(attributedlabel:attributedvalue:).md)
  Creates new custom content with an attributed string and attributed value.
- [convenience init(label: String, value: String)](axcustomcontent/init(label:value:).md)
  Creates new custom content with a label and value.
- [init?(coder: NSCoder)](axcustomcontent/init(coder:).md)
### Defining custom content
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
- [AXCustomContent.Importance](axcustomcontent/importance-swift.enum.md)
  Objects that control the timing of content output.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [protocol AXCustomContentProvider](axcustomcontentprovider.md)
  The interface for customizing the accessibility content.
- [typealias AXCustomContentReturnBlock](axcustomcontentreturnblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axcustomcontent)*