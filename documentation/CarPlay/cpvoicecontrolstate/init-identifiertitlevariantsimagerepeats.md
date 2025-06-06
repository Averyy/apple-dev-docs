# init(identifier:titleVariants:image:repeats:)

**Framework**: CarPlay  
**Kind**: init

Creates a voice control state.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(identifier: String, titleVariants: [String]?, image: UIImage?, repeats: Bool)
```

#### Return Value

A newly initialized voice control state.

## Parameters

- `identifier`: A string that your app uses to identify the state. You can activate the state by calling  , passing in the  .
- `titleVariants`: An array of title variants for the voice control state. When the system displays the title, it selects the title that best fits the available screen space, so arrange the titles from most to least preferred. Also, localize each title for display to the user, and be sure to include at least one title in the array.
- `image`: An image, no bigger than 150 pt x 150 pt, that the voice control template displays when it’s in this state. For an animated image, the system enforces a minimum cycle duration of 0.3 seconds, and a maximum cycle duration of 5 seconds.
- `repeats`: A Boolean value that indicates whether animation for   repeats indefinitely. Set to   to repeat the animation, or   to show the animation only once.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpvoicecontrolstate/init(identifier:titlevariants:image:repeats:))*