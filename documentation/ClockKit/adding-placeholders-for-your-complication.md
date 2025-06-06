# Adding Placeholders for Your Complication

**Framework**: ClockKit

Provide the placeholders that users see when adding your complication to a watch face.

#### Overview

Create placeholders for all of the complication families that your app supports. Ideally, these placeholders should indicate the type of data that your complication usually shows. The system uses these placeholders to represent your complication when the user configures a watch face on Apple Watch.

![A screenshot showing the placeholder for the Moon complication.](https://docs-assets.developer.apple.com/published/39f8980806ddcd864ddd6232bb39f4ed/media-3136367%402x.png)

You can provide placeholders in two ways: you can use static images for your placeholder, or dynamically create localized versions of the placeholders using complication templates. Ideally, your app provides both.

##### Add Static Placeholder Images

When you first install your app, the system initially displays the static placeholders. The system then checks to see if your data source can generate a localized placeholder using a complication template. If the data source returns a valid template, the system transitions from the static image to the localized placeholder. The system then caches the template, and reuses the cached version until the user updates or reinstalls your app.

If you don’t provide any placeholders, the system generates a placeholder based on your app icon.

By default, when you create a new watchOS project, or add a watchOS target to an existing project, Xcode adds a Complication group to your WatchKit extension’s asset catalog.

![A screenshot showing the WatchKit Extension’s complication group in the Assets catalog. This group includes placeholders for all the Apple Watch sizes supported by each complication family.](https://docs-assets.developer.apple.com/published/27b75dfef06e17e152bd5945c48ae608/media-3161750%402x.png)

Create PNG files to represent a complication for each family your app supports. Avoid using interlaced PNGs. Many complications use only the alpha channel of the image; however, graphic complications use full color images. For more information, see the [`Complications`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/watchos/overview/complications/) section of the Human Interface Guidelines.

Drag these files into the asset catalog, and drop them into the desired position. You can provide separate images for each screen size. If you don’t provide an image for a particular screen size, watchOS resizes the closest available image in that family.

##### Create Localized Placeholders

To dynamically create a localized placeholder, implement your data source’s [`getLocalizableSampleTemplate(for:withHandler:)`](clkcomplicationdatasource/getlocalizablesampletemplate(for:withhandler:).md) method. In your implementation, check the complication’s family, and create a template for that family. Populate the template with mock data that reflects what your complication would normally look like.

To localize the strings in your placeholder, use a simple text provider.

```swift
CLKSimpleTextProvider.localizableTextProvider(withStringsFileTextKey: "AKey")
```

The key must appear in a localized strings file named `ckcomplication.strings`. Save a copy of this strings file in your complication bundle and your WatchKit extension bundle. For more information, see [`Internationalization`](https://developer.apple.comhttps://developer.apple.com/internationalization/).

## See Also

- [Declaring complications for your app](declaring-complications-for-your-app.md)
  Define the complications that your app supports.
- [Creating a timeline entry](creating-a-timeline-entry.md)
  Package your app-specific data into a template and create a timeline entry for that template.
- [Loading future timeline events](loading-future-timeline-events.md)
  Preserve battery life and improve performance on the watch by providing a timeline with expected data and updates.
- [Keeping your complications up to date](keeping-your-complications-up-to-date.md)
  Replace or extend the data in your complication’s timeline.
- [Enabling Complications for Your watchOS App](enabling-complications-for-your-watchos-app.md)
  Set up your watchOS app’s complications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/adding-placeholders-for-your-complication)*