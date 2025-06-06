# barStyle

**Framework**: UIKit  
**Kind**: property

The navigation bar style that specifies its appearance.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var barStyle: UIBarStyle { get set }
```

#### Discussion

See [`UIBarStyle`](uibarstyle.md) for possible values. The default value is [`UIBarStyle.default`](uibarstyle/default.md).

It is permissible to set the value of this property when the navigation bar is being managed by a navigation controller object.

## See Also

- [enum UIBarStyle](uibarstyle.md)
  Defines the stylistic appearance of different types of views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbar/barstyle)*