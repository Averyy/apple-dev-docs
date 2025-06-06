# identifier

**Framework**: CarPlay  
**Kind**: property

The string that your app uses to identify the voice control state.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var identifier: String { get }
```

#### Discussion

Use [`identifier`](cpvoicecontrolstate/identifier.md) when calling the [`activateVoiceControlState(withIdentifier:)`](cpvoicecontroltemplate/activatevoicecontrolstate(withidentifier:).md) method to activate the voice control state.

## See Also

- [var titleVariants: [String]?](cpvoicecontrolstate/titlevariants.md)
  The array of title variants for the voice control state.
- [var image: UIImage?](cpvoicecontrolstate/image.md)
  The image displayed while the voice control template is in this state.
- [var repeats: Bool](cpvoicecontrolstate/repeats.md)
  A Boolean value that indicates whether the display of an animated image repeats the animation sequence indefinitely.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpvoicecontrolstate/identifier)*