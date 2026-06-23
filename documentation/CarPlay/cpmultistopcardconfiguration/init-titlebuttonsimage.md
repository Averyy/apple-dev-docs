# init(title:buttons:image:)

**Framework**: CarPlay  
**Kind**: init

Initializes a MultiStopCardConfiguration with an optional title, an array of text buttons, and an optional image

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
init(title: String?, buttons: [CPTextButton], image: UIImage?)
```

#### Discussion

Your app should provide a @c UIImage that is display-ready, containing two @c UIImageAssets, corresponding to night and day mode.

When providing an image, your app should provide a @c UIImage that is display-ready. If necessary for the image, provide light and dark styles by using an asset from your asset catalog, prepared with light and dark styles or by using @c UIImageAsset to combine two @c UIImage instances into a single image with both styles.

UIImageAsset is used to combine multiple UIImages with different trait collections into a single UIImage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmultistopcardconfiguration/init(title:buttons:image:))*