# focused

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The appearance data to apply to the button when it’s focused.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var focused: UIBarButtonItemStateAppearance { get }
```

```objc
@property (nonatomic, strong, readonly) UIBarButtonItemStateAppearance * focused;
```

#### Discussion

To set the attributes for this state, get the object in this property and modify it.

## See Also

### Configuring attributes for different button states
- [var normal: UIBarButtonItemStateAppearance](./normal.md)
  The appearance data to apply to the button when it’s in the normal state.
- [var disabled: UIBarButtonItemStateAppearance](./disabled.md)
  The appearance data to apply to the button when it’s in the disabled state.
- [var highlighted: UIBarButtonItemStateAppearance](./highlighted.md)
  The appearance data to apply to the button when it’s in the highlighted state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitemappearance/focused)*