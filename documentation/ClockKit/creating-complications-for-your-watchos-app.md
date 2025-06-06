# Creating complications for your watchOS app

**Framework**: ClockKit

Set up and implement complications for your watchOS app.

#### Overview

Complications are small interface elements that users place on the clock face.

![An image of an Infographic Modular watch face with the complications highlighted. The face uses graphic circular templates for the Weather, Breathe, Air Quality Index, and Workout apps. It uses a graphic large image template for the Heart Rate app.](https://docs-assets.developer.apple.com/published/e8681f07a11801363b1601f240bc5ccc/media-3598123%402x.png)

Having your complication on an active watch face gives you the opportunity to provide useful data whenever the user glances at their watch. Users can also interact with your app by tapping on the complication and launching your app. The system also provides apps with active complications larger budgets for background refresh tasks. You can use these tasks to keep the content of your watchOS app and your complications up to date and accurate.

##### Add Complications to Your App

To add complications to your watchOS app, perform the following steps:

1. Select the data to display.
2. Enable complications for your App.
3. Implement your data source.
4. Update your complications.
5. Add placeholders for your complications.

##### Select the Data to Display

Before creating a complication, decide on the data you want to display. Each watch face only provides space for a handful of complications, and users are more likely to add your complication if it provides useful and up-to-date information at a glance.

Consider the following:

The system gives larger background budgets to watchOS apps with complications on the active watch face. However, it still limits the background tasks to about four tasks per hour. Alternatively, you can generate the complication data on your server, and send it to the watch using push notifications. This strategy lets you move complex and time consuming tasks off the watch; however, the system limits you to 50 complication push notifications per day. Be sure that your complications can provide useful and timely information within these constraints.

##### Set Up and Design Your Complications

Before you can begin designing your complications, you need to enable support. If you’re creating a new project, you can choose to include complications in the project, and Xcode does all the work for you. However, if you want to add complications to an existing app, you may need to create and configure your complications’ data source and an asset group. For more information, see [`Enabling Complications for Your watchOS App`](enabling-complications-for-your-watchos-app.md).

Next, implement your app’s data source. ClockKit calls the [`CLKComplicationDataSource`](clkcomplicationdatasource.md) protocol’s methods to request information about the complications your app supports, and to fill the timeline of any complications on an active watch face. For more information, see [`Declaring complications for your app`](declaring-complications-for-your-app.md), [`Creating a timeline entry`](creating-a-timeline-entry.md), and [`Loading future timeline events`](loading-future-timeline-events.md).

Finally, an effective complication must display useful information whenever the user glances at it. For information on strategies to keep your complication up to date and accurate, see [`Keeping your complications up to date`](keeping-your-complications-up-to-date.md).

##### Add Placeholders

ClockKit displays placeholders for your app’s complications while the user configures a watch face. Your app can provide static images and localized templates as placeholders. For static placeholders, place images in the Complications group in your watch extension’s assets catalog. For localized templates, implement your data source’s [`getLocalizableSampleTemplate(for:withHandler:)`](clkcomplicationdatasource/getlocalizablesampletemplate(for:withhandler:).md) method.

ClockKit uses the localizable templates whenever possible; however, it may display the static image if the template isn’t available, such as when the user first installs your app. For more information, see [`Adding Placeholders for Your Complication`](adding-placeholders-for-your-complication.md).

##### Test Your Complications

To test your complications, build and install the app on the simulator or a test device. Then add the complication to an active watch face, as described in this example:

1. Build and run the sample code project.
2. Press the Digital Crown to return to the watch face.
3. Firmly press the watch face to configure it, then tap Customize.
4. Swipe left until the complications are highlighted. Select the complication you want to modify.
5. Scroll to select your app’s complication.
6. Press the Digital Crown again to save your changes.

For more information on configuring watch faces, see [`Change the watch face on your Apple Watch`](https://developer.apple.comhttps://support.apple.com/en-us/HT205536).

If you included complications when you created the project, Xcode automatically creates a scheme for installing and debugging your complications. By default, the scheme’s name ends in “WatchKit App (Complication)”. When you run this scheme, Xcode installs the latest version of your app and reloads your complications. You can set breakpoints in your complication’s data source to step through the loading process.

## Topics

### Configure Complications
- [Enabling Complications for Your watchOS App](enabling-complications-for-your-watchos-app.md)
  Set up your watchOS app’s complications.
- [Adding Placeholders for Your Complication](adding-placeholders-for-your-complication.md)
  Provide the placeholders that users see when adding your complication to a watch face.

## See Also

- [Declaring complications for your app](declaring-complications-for-your-app.md)
  Define the complications that your app supports.
- [Creating a timeline entry](creating-a-timeline-entry.md)
  Package your app-specific data into a template and create a timeline entry for that template.
- [Loading future timeline events](loading-future-timeline-events.md)
  Preserve battery life and improve performance on the watch by providing a timeline with expected data and updates.
- [Keeping your complications up to date](keeping-your-complications-up-to-date.md)
  Replace or extend the data in your complication’s timeline.
- [Building complications with SwiftUI](building-complications-with-swiftui.md)
  Design the appearance of a graphic complication using SwiftUI.
- [Displaying progress views and gauges](displaying-progress-views-and-gauges.md)
  Add rich visual data to your SwiftUI complications with progress views and gauges.
- [Adding text to a complication](adding-text-to-a-complication.md)
  Use text in SwiftUI complications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/creating-complications-for-your-watchos-app)*