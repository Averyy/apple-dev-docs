# Responding to changing display modes on Apple TV

**Framework**: UIKit

Change images and resources dynamically when the screen gamut on your device changes.

#### Overview

On Apple TV (5th generation), the assets required for an app depend on the screen gamut of the TV being used, with 4K TVs using the Display P3 gamut, and all other resolutions using the sRGB gamut. Also, the screen gamut of the TV can change at any time, switching between 4K and other resolutions. Your app needs to respond to these changes and present the appropriate assets when required.

##### Create and Place the Image Assets

In Xcode, create an image asset in an asset catalog. In the Attributes inspector, configure the asset catalog to handle Display P3 images. In the Devices pane, ensure that Apple TV is selected. From the Gamut menu, select sRGB and Display P3. The following image shows the correct settings.

![Screenshot that shows the asset catalog configuration for sRGB and Display P3 image support.](https://docs-assets.developer.apple.com/published/e7a1b5d6bf0f076668304f0c491d62c7/media-2923968%402x.png)

##### Add Images to the Asset Catalog

Place non-4K images in the 1x (sRGB) slot and 4K images in the 2x (Display P3) slot. The correct image is automatically loaded based on the display gamut of the TV. The following image shows assets placed in their correct containers.

![Screenshot that shows adding 1x and 2x assets to their corresponding slots in an asset catalog.](https://docs-assets.developer.apple.com/published/6e955362b1eda0595260faf77569eb5a/media-2930448%402x.png)

##### Adapt to Screen Changes Programmatically

Implement the [`traitCollectionDidChange(_:)`](uitraitenvironment/traitcollectiondidchange(_:).md) method to respond to changing device traits. If your app performs expensive operations related to image generation based on the current display gamut, it’s important to verify that the display gamut has changed before performing these operations. The following code shows how to test whether the display gamut changed.

```swift
override func traitCollectionDidChange(_ previousTraitCollection: UITraitCollection?) {
    let currentDisplayGamut = self.traitCollection.displayGamut
    if (previousTraitCollection?.displayGamut == .SRGB) && (currentDisplayGamut == .SRGB) {
        // Resolution didn't change. Your code goes here.
    } else if (previousTraitCollection?.displayGamut == .P3) && (currentDisplayGamut == .P3) {
        // Resolution didn't change. Your code goes here.
    } else {
        // Resolution changed. Your code goes here.
    }
}
```

## See Also

- [Traits and the trait environment](traits-and-the-trait-environment.md)
  Get information about traits and the environment in which your app runs, and share data with your view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/responding-to-changing-display-modes-on-apple-tv)*