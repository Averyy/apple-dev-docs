# tintColor

**Framework**: ClockKit  
**Kind**: property

The tint color to apply to elements of the template.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@NSCopying
var tintColor: UIColor? { get set }
```

#### Discussion

The color in this property is the default color applied to images and highlighted text in the template. This color is applied only on clock faces that support multiple colors and only when the text or image provider doesn’t provide a custom color. If the value in this property is `nil`, ClockKit uses white for the default color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplate/tintcolor)*