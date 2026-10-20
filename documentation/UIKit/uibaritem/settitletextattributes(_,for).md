# setTitleTextAttributes(_:for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the title’s text attributes for a given control state.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setTitleTextAttributes(_ attributes: [NSAttributedString.Key : Any]?, for state: UIControl.State)
```

```objc
- (void) setTitleTextAttributes:(NSDictionary<NSString *,id> *) attributes forState:(UIControlState) state;
```

## Parameters

- `attributes`: A dictionary containing key-value pairs for text attributes.

  You can specify the font, text color, text shadow color, and text shadow offset using the keys listed in NSString UIKit Additions Reference.
- `state`: The control state for which you want to set the text attributes for the title.

## See Also

### Customizing appearance
- [func titleTextAttributes(for: UIControl.State) -> [NSAttributedString.Key : Any]?](./titletextattributes%28for%29.md)
  Returns the title’s text attributes for a given control state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibaritem/settitletextattributes(_:for:))*