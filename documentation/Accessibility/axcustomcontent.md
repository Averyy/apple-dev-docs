# AXCustomContent

**Framework**: Accessibility  
**Kind**: class  
**Role**: Class

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

```objc
@interface AXCustomContent : NSObject
```

## Overview

An `AXCustomContent` object contains the accessibility strings for the labels you apply to your accessibility content. Combine them with the [`AXCustomContentProvider`](./axcustomcontentprovider.md) protocol to allow your users to experience the content in a more appropriate manner for each assistive technology.

## Topics

### Creating custom content
- [convenience init(attributedLabel: NSAttributedString, attributedValue: NSAttributedString)](./axcustomcontent/init%28attributedlabel,attributedvalue%29.md)
  Creates new custom content with an attributed string and attributed value.
- [convenience init(label: String, value: String)](./axcustomcontent/init%28label,value%29.md)
  Creates new custom content with a label and value.
- [init?(coder: NSCoder)](./axcustomcontent/init%28coder%29.md)
### Defining custom content
- [var label: String](./axcustomcontent/label.md)
  A localized string that identifies the label for this content.
- [var attributedLabel: NSAttributedString](./axcustomcontent/attributedlabel.md)
  A localized attributed string that identifies the label for this content.
- [var value: String](./axcustomcontent/value.md)
  A localized string that provides a value for the label.
- [var attributedValue: NSAttributedString](./axcustomcontent/attributedvalue.md)
  A localized attributed string that provides a value for the label.
- [var importance: AXCustomContent.Importance](./axcustomcontent/importance-swift.property.md)
  An object that determines when to output custom accessibility content.
- [AXCustomContent.Importance](./axcustomcontent/importance-swift.enum.md)
  Objects that control the timing of content output.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Custom accessibility content
- [protocol AXCustomContentProvider](./axcustomcontentprovider.md)
  The interface for customizing the accessibility content.
- [typealias AXCustomContentReturnBlock](./axcustomcontentreturnblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axcustomcontent)*