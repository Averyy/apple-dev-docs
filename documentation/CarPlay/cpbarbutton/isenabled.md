# isEnabled

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the button is enabled.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var isEnabled: Bool { get set }
```

```objc
@property (nonatomic, assign, getter=isEnabled) BOOL enabled;
```

## Discussion

When the value of this property is `true`, the button displays an enabled appearance and calls the attached handler in response to interactions. When the value of this property is `false`, the button displays a disabled appearance and doesn’t call the attached handler. The default value of this property is `true`.

## See Also

### Configuring the button
- [var image: UIImage?](./image.md)
  The image to display in the button.
- [var title: String?](./title.md)
  The text to display in the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpbarbutton/isenabled)*