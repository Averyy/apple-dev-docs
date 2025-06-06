# image

**Framework**: CarPlay  
**Kind**: property

The image displayed while the voice control template is in this state.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var image: UIImage? { get }
```

#### Discussion

For the animated images, the system enforces a minimum cycle duration of 0.3 seconds, and a maximum cycle duration of 5 seconds.

## See Also

- [var identifier: String](cpvoicecontrolstate/identifier.md)
  The string that your app uses to identify the voice control state.
- [var titleVariants: [String]?](cpvoicecontrolstate/titlevariants.md)
  The array of title variants for the voice control state.
- [var repeats: Bool](cpvoicecontrolstate/repeats.md)
  A Boolean value that indicates whether the display of an animated image repeats the animation sequence indefinitely.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpvoicecontrolstate/image)*