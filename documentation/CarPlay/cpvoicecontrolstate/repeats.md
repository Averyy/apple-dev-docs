# repeats

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the display of an animated image repeats the animation sequence indefinitely.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var repeats: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL repeats;
```

#### Discussion

The animation repeats when this property is [`true`](../../Swift/true.md); otherwise, animation occurs only once.

## See Also

### Getting State Information
- [var identifier: String](./identifier.md)
  The string that your app uses to identify the voice control state.
- [var titleVariants: [String]?](./titlevariants.md)
  The array of title variants for the voice control state.
- [var image: UIImage?](./image.md)
  The image displayed while the voice control template is in this state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpvoicecontrolstate/repeats)*