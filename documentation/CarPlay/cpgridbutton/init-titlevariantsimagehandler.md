# init(titleVariants:image:handler:)

**Framework**: CarPlay  
**Kind**: init

Creates a grid button with the specified title variants, image, and action handler.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
convenience init(titleVariants: [String], image: UIImage, handler: ((CPGridButton) -> Void)? = nil)
```

#### Return Value

A newly initialized grid button.

## Parameters

- `titleVariants`: An array of title variants for the button. Each title should be localized and ready for display to the user. When the system displays the button, it selects the title that best fits the available screen space, so arrange the variants from most to least preferred. Always include at least one title in the array.
- `image`: The image to display on the button. If you provide an animated image, the button uses the first image in the animation sequence.
- `handler`: The block invoked after the user taps the button. In Swift, the default is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpgridbutton/init(titlevariants:image:handler:))*