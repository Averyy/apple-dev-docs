# init(textElement:range:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Create a new layout fragment using the provided text element and range.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
init(textElement: NSTextElement, range rangeInElement: NSTextRange?)
```

```objc
- (instancetype) initWithTextElement:(NSTextElement *) textElement range:(NSTextRange *) rangeInElement;
```

## Parameters

- `textElement`: An [`NSTextElement`](../nstextelement.md).
- `rangeInElement`: A range that defines the boundaries of the text for the new layout fragment.

## See Also

### Creating a layout fragment
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a new layout fragment with the coder you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutfragment/init(textelement:range:))*