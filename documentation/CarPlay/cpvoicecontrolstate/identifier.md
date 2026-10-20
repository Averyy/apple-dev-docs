# identifier

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The string that your app uses to identify the voice control state.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var identifier: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * identifier;
```

#### Discussion

Use [`identifier`](./identifier.md) when calling the [`activateVoiceControlState(withIdentifier:)`](../cpvoicecontroltemplate/activatevoicecontrolstate%28withidentifier%29.md) method to activate the voice control state.

## See Also

### Getting State Information
- [var titleVariants: [String]?](./titlevariants.md)
  The array of title variants for the voice control state.
- [var image: UIImage?](./image.md)
  The image displayed while the voice control template is in this state.
- [var repeats: Bool](./repeats.md)
  A Boolean value that indicates whether the display of an animated image repeats the animation sequence indefinitely.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpvoicecontrolstate/identifier)*