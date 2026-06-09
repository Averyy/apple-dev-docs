# init(identifier:titleVariants:image:backgroundImage:repeats:)

**Framework**: CarPlay  
**Kind**: init

Initialize a voice control state with a title and image.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
init(identifier: String, titleVariants: [String]?, image: UIImage?, backgroundImage: UIImage?, repeats: Bool)
```

#### Discussion

When providing an image, your app should provide a @c UIImage that is display-ready. If necessary for the image, provide light and dark styles by using an asset from your asset catalog, prepared with light and dark styles or by using @c UIImageAsset to combine two @c UIImage instances into a single image with both styles.

## Parameters

- `identifier`: A custom identifier you can use to identify this voice control state. You’ll also switch to this state by specifying this identifier.
- `titleVariants`: An array of title variants. The Voice Control template will select the longest variant that fits your specified content.
- `image`: An image to be animated while this template is visible. The system enforces a minimum cycle duration of 0.3 seconds and a maximum cycle duration of 5 seconds. Voice Control state images may be a maximum of 150 by 150 points.
- `backgroundImage`: A custom background image to be displayed behind the voice control template content. The background image fills the entire template view and appears behind all voice control state content, including the state image, title variants, and action buttons.
- `repeats`: For an animated image, YES if the animation should repeat indefinitely, NO to run the animation only once.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpvoicecontrolstate/init(identifier:titlevariants:image:backgroundimage:repeats:))*