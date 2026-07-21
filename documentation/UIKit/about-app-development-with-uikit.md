# About app development with UIKit

**Framework**: UIKit

Learn about the basic support that UIKit and Xcode provide for your iOS and tvOS apps.

#### Overview

The UIKit framework provides the core objects that you need to build apps for iOS and tvOS. You use these objects to display your content onscreen, to interact with that content, and to manage interactions with the system. Apps rely on UIKit for their basic behavior, and UIKit provides many ways for you to customize that behavior to match your specific needs.

> ❗ **Important**:  Start the development of an iOS or tvOS app by creating a project in Xcode, Apple’s integrated development environment. If you don’t have Xcode, you can download it from the App Store. You can also download the latest version from [`developer.apple.com/downloads`](https://developer.apple.comhttps://developer.apple.com/downloads).

Xcode provides template projects as starting points for every app you create. For example, the following image shows the structure of an app created using the iOS app template in Xcode. The template projects provide a minimal user interface, so you can build and run your project immediately and see the results on a device or in the simulator.

![A partial screenshot of Project navigator in Xcode that shows a template for a new single view app. The app contains source files for an app delegate, scene delegate, and view controller. It also contains storyboard, asset catalog, and Info.plist files.](https://docs-assets.developer.apple.com/published/075f4171b78405b89507bb6e9ecb616c/about-app-development-with-uikit-1%402x.png)

When you build your app, Xcode compiles your source files and creates an app bundle for your project. An app bundle is a structured directory that contains the code and resources associated with the app. Resources include the image assets, storyboard files, strings files, and app metadata that support your code.

##### Add Required Resources

Every UIKit app is required to have the following resources:

- App icons
- Launch screen storyboard

The system displays your app icon on the Home Screen, in Settings, and anywhere it needs to differentiate your app from other apps. Because it may display in dark or light appearance, or a person may choose the tinted display option, you provide multiple versions of your app icon in your Xcode project’s AppIcon image asset. Create a distinctive app icon to help people quickly identify your app on the Home Screen. Test different appearances and display options to determine if you need to vary the details of your icon. For more information, see [`Creating your app icon using Icon Composer`](https://developer.apple.com/documentation/Xcode/creating-your-app-icon-using-icon-composer) and [`Configuring your app icon using an asset catalog`](https://developer.apple.com/documentation/Xcode/configuring-your-app-icon).

![A screenshot of an asset catalog in Xcode that shows the variants for the app's icon.](https://docs-assets.developer.apple.com/published/563356d47201ebde749ad32bffc1a2b2/about-app-development-with-uikit-2%402x.png)

The `LaunchScreen.storyboard` file contains your app’s initial interface, and it can be a splash screen or a simplified version of your actual interface. When someone taps your app’s icon, the system displays your launch screen immediately, letting the person know that your app is now launching. The launch screen also provides cover for your app while it initializes itself. When your app is ready, the system hides the launch screen and reveals your app’s actual interface. For more information, see [`Specifying your app’s launch screen`](https://developer.apple.com/documentation/Xcode/specifying-your-apps-launch-screen).

##### Update Required App Metadata

The system derives information about your app’s configuration and capabilities from the information property list. Xcode provides a preconfigured version of this list with every new project template, and you modify it based on the needs of your app. For example, if your app relies on specific hardware, or uses specific system frameworks, you can add information related to those features to the list.

One common modification you can make to the information property list is to declare your app’s hardware and software requirements. These requirements are how you communicate to the system what your app needs to run. For example, a navigation app might require the presence of GPS hardware to provide turn-by-turn directions. The App Store prevents someone from installing your app on a device that doesn’t meet your app’s requirements.

![A screenshot of the Info tab in Xcode showing custom iOS target properties. The device capabilities include information such as whether the app requires a camera, location services, or a particular technology.](https://docs-assets.developer.apple.com/published/b080cd91860e85e9018d4432fcd7a80c/about-app-development-with-uikit-3%402x.png)

For information about the keys that you can include in your information property list, see [`Information Property List`](https://developer.apple.com/documentation/BundleResources/Information-Property-List).

##### Review the Code Structure of a Uikit App

UIKit provides many of your app’s core objects, including those that interact with the system, run the app’s main event loop, and display your content onscreen. You use most of these objects as-is or with only minor modifications. Knowing which objects to modify, and when to modify them, is crucial to implementing your app.

Your app uses [`UIApplication`](uiapplication.md) and a [`UIApplicationDelegate`](uiapplicationdelegate.md) subclass to interact with application-level services and information. You configure and customize one or more [`Scenes`](scenes.md) to present your app on the screen. Use multiple scenes to represent multiple instances of your app or to handle showing your app on a noninteractive external display.

The structure of UIKit apps is based on the Model-View-Controller (MVC) design pattern, where you create objects that fulfill specific purposes. Model objects manage the app’s data and business logic. View objects provide the visual representation of your data. Controller objects act as a bridge between your model and view objects, moving data between them at appropriate times.

##### Build and Organize Your App with Uikit Objects

The UIKit and Foundation frameworks provide many of the basic types that you use to define your app’s model objects. UIKit provides a [`UIDocument`](uidocument.md) object for organizing the data structures that belong in a disk-based file. The Foundation framework defines basic objects representing strings, numbers, arrays, and other data types. The [`Swift Standard Library`](https://developer.apple.com/documentation/Swift/swift-standard-library) provides many of the same types available in the Foundation framework.

UIKit provides controller objects to help you organize and move between your views. [`UIViewController`](uiviewcontroller.md) is the basic controller object you subclass to manage and display a view. Implement common user interface designs with controllers like [`UINavigationController`](uinavigationcontroller.md), [`UISplitViewController`](uisplitviewcontroller.md), and [`UITabBarController`](uitabbarcontroller.md). For more information, see [`View controllers`](view-controllers.md).

Build views with [`UIView`](uiview.md), which displays your content onscreen. Lay out your views with [`UIStackView`](uistackview.md), or use Auto Layout for more complex layouts. Make your app responsive to size changes using details in [`View layout`](view-layout.md). Use objects like [`UIScrollView`](uiscrollview.md), [`UITableView`](uitableview.md), and [`UICollectionView`](uicollectionview.md) to efficiently lay out multiple views, or to display views for more data than can fit on the screen at one time.

Manage and respond to interactions with [`UIControl`](uicontrol.md) objects, such as [`UIButton`](uibutton.md), [`UISlider`](uislider.md), and [`UISegmentedControl`](uisegmentedcontrol.md). Use views such as [`UICalendarView`](uicalendarview.md), [`UIImageView`](uiimageview.md), and [`UIPickerView`](uipickerview.md) to display and interact with specific types of data. Update your views in response to long presses, pans, swipes, pinches, and other gestures with [`UIGestureRecognizer`](uigesturerecognizer.md) and related subclasses.

Show and interact with text using [`UILabel`](uilabel.md), [`UITextField`](uitextfield.md), and [`UITextView`](uitextview.md). For more information, see [`Views and controls`](views-and-controls.md).

## See Also

- [Adopting Liquid Glass](../TechnologyOverviews/adopting-liquid-glass.md)
  Find out how to bring the new material to your app.
- [UIKit updates](../Updates/UIKit.md)
  Learn about important changes to UIKit.
- [Protecting the User’s Privacy](protecting-the-user-s-privacy.md)
  Secure personal data, and respect user preferences for how data is used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/about-app-development-with-uikit)*