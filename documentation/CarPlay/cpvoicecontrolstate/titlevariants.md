# titleVariants

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The array of title variants for the voice control state.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var titleVariants: [String]? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<NSString *> * titleVariants;
```

## Discussion

When creating a voice control state, arrange the titles from most to least preferred. The system displays the first title found in the array that best fits the available screen space. Also, localize each title for display to the user, and be sure to include at least one title in the array.

## See Also

### Getting State Information
- [var identifier: String](./identifier.md)
  The string that your app uses to identify the voice control state.
- [var image: UIImage?](./image.md)
  The image displayed while the voice control template is in this state.
- [var repeats: Bool](./repeats.md)
  A Boolean value that indicates whether the display of an animated image repeats the animation sequence indefinitely.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpvoicecontrolstate/titlevariants)*