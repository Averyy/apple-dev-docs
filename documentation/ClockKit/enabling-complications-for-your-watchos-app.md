# Enabling Complications for Your watchOS App

**Framework**: ClockKit

Set up your watchOS app’s complications.

#### Overview

Before adding complications to the Apple Watch face, you must enable support for them in your app. You can include the complications when you create a new app, or add complications to an existing app.

##### Include Complications in a New App

Check Include Complications to enable complications when creating a new watchOS app, as shown in the figure below.

![The option sheet with the Include Complications option enabled.](https://docs-assets.developer.apple.com/published/dd914075d9bb5b7a4d7623b12e99224e/media-3570873%402x.png)

When you include complications, Xcode creates and configures a complication data source for your app. The data source includes stubs for many of the methods required to configure your complications, populate your timeline, and provide placeholders. Xcode also creates a group in your extension’s assets catalog for static placeholder images.

##### Add Complications to an Existing App

To add complications to an existing watchOS app, you need to create these items yourself. Start by creating a class that adopts the [`CLKComplicationDataSource`](clkcomplicationdatasource.md) protocol.

```swift
import Foundation
import ClockKit

class ComplicationController: NSObject, CLKComplicationDataSource {

    func getCurrentTimelineEntry(for complication: CLKComplication, withHandler handler: @escaping (CLKComplicationTimelineEntry?) -> Void) {
        // TODO: Finish implementing this required method.
    }
}
```

Next, add a Complication group to your extension’s assets catalog (if one doesn’t already exist). Open the `Assets.xcassets` file and select Editor > Add Assets > watchOS > New Watch Complication Placeholder, as in the figure below.

![A screenshot of the Complication group in the extension’s assets catalog.](https://docs-assets.developer.apple.com/published/5961ba6f8d73bdf3abc4a67bf2ff9831/media-3570878%402x.png)

Finally, select your app in the Project navigator, and open the extension’s General tab. In the Complication Configuration set the Data Source Class and Complication Group to the class and asset catalog group you just created.

![A screenshot that shows the complication configuration settings, with the data source and asset group specified.](https://docs-assets.developer.apple.com/published/915fc68d76d59d24bfa79eef6870cfa1/media-3570877%402x.png)

## See Also

- [Declaring complications for your app](declaring-complications-for-your-app.md)
  Define the complications that your app supports.
- [Creating a timeline entry](creating-a-timeline-entry.md)
  Package your app-specific data into a template and create a timeline entry for that template.
- [Loading future timeline events](loading-future-timeline-events.md)
  Preserve battery life and improve performance on the watch by providing a timeline with expected data and updates.
- [Keeping your complications up to date](keeping-your-complications-up-to-date.md)
  Replace or extend the data in your complication’s timeline.
- [Adding Placeholders for Your Complication](adding-placeholders-for-your-complication.md)
  Provide the placeholders that users see when adding your complication to a watch face.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/enabling-complications-for-your-watchos-app)*