# titleTextAttributes(for:)

**Framework**: UIKit  
**Kind**: method

Returns the title’s text attributes for a given control state.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func titleTextAttributes(for state: UIControl.State) -> [NSAttributedString.Key : Any]?
```

#### Return Value

The title’s text attributes for `state`.

#### Discussion

The dictionary may contain key-value pairs for text attributes for the font, text color, text shadow color, and text shadow offset using the keys listed in NSString UIKit Additions Reference.

## Parameters

- `state`: The control state for which you want to know the text attributes for the title.

## See Also

- [func setTitleTextAttributes([NSAttributedString.Key : Any]?, for: UIControl.State)](uibaritem/settitletextattributes(_:for:).md)
  Sets the title’s text attributes for a given control state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibaritem/titletextattributes(for:))*