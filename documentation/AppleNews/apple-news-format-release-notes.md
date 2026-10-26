# Apple News Format Release Notes

**Framework**: Apple News  
**Role**: Article

Learn about new features that require iOS 26, iPadOS 26, and macOS 26.

#### Overview

This feature was added for the latest Apple News Format release:

- In the [`Metadata`](https://developer.apple.com/documentation/applenewsformat/metadata) object, use `syndicated` to indicate a syndication or wire service produced the content.

These features were added in a previous Apple News Format release:

- You can embed a Facebook reel in your article using the `URL` property in the [`FacebookPost`](https://developer.apple.com/documentation/applenewsformat/facebookpost) object.
- In the [`Condition`](https://developer.apple.com/documentation/applenewsformat/condition) object, use `following` to indicate whether the person viewing the article is following the channel that published the article.

##### Deprecated Objects and Properties

This property was deprecated in the latest Apple News Format release:

- The `transparentToolbar` property in the [`Metadata`](https://developer.apple.com/documentation/applenewsformat/metadata) object was deprecated.

These objects were deprecated in a previous Apple News Format release:

- [`AutoPlacement`](https://developer.apple.com/documentation/applenewsformat/autoplacement), [`AdvertisementAutoPlacement`](https://developer.apple.com/documentation/applenewsformat/advertisementautoplacement), [`ConditionalAutoPlacement`](https://developer.apple.com/documentation/applenewsformat/conditionalautoplacement), and [`AutoPlacementLayout`](https://developer.apple.com/documentation/applenewsformat/autoplacementlayout) objects are deprecated because you can only control advertisement settings via News Publisher.
- [`MediumRectangleAdvertisement`](https://developer.apple.com/documentation/applenewsformat/mediumrectangleadvertisement) and [`BannerAdvertisement`](https://developer.apple.com/documentation/applenewsformat/banneradvertisement) objects are deprecated because Apple News no longer supports manual ads.

## See Also

### Release Notes
- [Apple News Format Version History](./apple-news-format-version-history.md)
  Learn how Apple News Format versions map to iOS, iPadOS, macOS, and visionOS releases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/apple-news-format-release-notes)*