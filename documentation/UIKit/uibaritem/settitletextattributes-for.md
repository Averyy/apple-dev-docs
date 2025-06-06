# setTitleTextAttributes(_:for:)

**Framework**: UIKit  
**Kind**: method

Sets the title’s text attributes for a given control state.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setTitleTextAttributes(_ attributes: [NSAttributedString.Key : Any]?, for state: UIControl.State)
```

## Parameters

- `attributes`: You can specify the font, text color, text shadow color, and text shadow offset using the keys listed in NSString UIKit Additions Reference.
- `state`: The control state for which you want to set the text attributes for the title.

## See Also

- [func titleTextAttributes(for: UIControl.State) -> [NSAttributedString.Key : Any]?](uibaritem/titletextattributes(for:).md)
  Returns the title’s text attributes for a given control state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibaritem/settitletextattributes(_:for:))*