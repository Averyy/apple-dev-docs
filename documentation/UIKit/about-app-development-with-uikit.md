# About App Development with UIKit

**Framework**: UIKit

Learn about the basic support that UIKit and Xcode provide for your iOS and tvOS apps.

#### Overview

The UIKit framework provides the core objects that you need to build apps for iOS and tvOS. You use these objects to display your content onscreen, to interact with that content, and to manage interactions with the system. Apps rely on UIKit for their basic behavior, and UIKit provides many ways for you to customize that behavior to match your specific needs.

> ❗ **Important**:  You always start the development of an iOS or tvOS app by creating a project in Xcode, Apple’s integrated development environment. If you don’t have Xcode, you can download it from the App Store. You can also download the latest version from [`developer.apple.com`](https://developer.apple.comhttps://developer.apple.com).

 You always start the development of an iOS or tvOS app by creating a project in Xcode, Apple’s integrated development environment. If you don’t have Xcode, you can download it from the App Store. You can also download the latest version from [`developer.apple.com`](https://developer.apple.comhttps://developer.apple.com).

Xcode provides template projects as starting points for every app you create. For example, the following image shows the structure of an app created using the single view app template in Xcode. The template projects provide a minimal user interface, so you can build and run your project immediately and see the results on a device or in the simulator.

![The template for a new single view app contains source files for an app delegate and view controller. It also contains storyboard, asset catalog, and Info.plist files.](https://docs-assets.developer.apple.com/published/845c646f662306d96beb0e6ac9602b0a/media-3004316%402x.png)

When you build your app, Xcode compiles your source files and creates an app bundle for your project. An app bundle is a structured directory that contains the code and resources associated with the app. Resources include the image assets, storyboard files, strings files, and app metadata that support your code. The structure of the app bundle is important, but Xcode knows where your resources need to go, so don’t worry about it for now.

##### Required Resources

Every UIKit app is required to have the following resources:

- App icons
- Launch screen storyboard

The system displays your app icon on the Home screen, in Settings, and anywhere it needs to differentiate your app from other apps. Because it is used in multiple places, and on multiple devices, you provide multiple versions of your app icon in your Xcode project’s AppIcon image asset. Your app icon should be distinctive to help the user identify your app quickly on the Home screen. However, you may vary the details of your icon to accommodate the different image sizes that you must provide.

![An asset catalog contains many variants for the app’s icon.](https://docs-assets.developer.apple.com/published/701d4281f3734f46fabbcbf56ae22a1f/media-3004317%402x.png)

The `LaunchScreen.storyboard` file contains your app’s initial user interface, and it can be a splash screen or a simplified version of your actual interface. When the user taps your app’s icon, the system displays your launch screen immediately, letting the user know that your app is now launching. The launch screen also provides cover for your app while it initializes itself. When your app is ready, the system hides the launch screen and reveals your app’s actual interface.

##### Required App Metadata

The system derives information about your app’s configuration and capabilities from the information property list (`Info.plist`) file in your app bundle. Xcode provides a preconfigured version of this file with every new project template, but you will likely need to modify this file at some point. For example, if your app relies on specific hardware, or uses specific system frameworks, you might need to add information related to those features to this file.

One common modification you can make to the `Info.plist` file is to declare your app’s hardware and software requirements. These requirements are how you communicate to the system what your app needs to run. For example, a navigation app might require the presence of GPS hardware to provide turn-by-turn directions. The App Store prevents an app from being installed on a device that does not meet your app’s requirements.

![Device capabilities include information such as whether the app requires a camera, location services, or a particular technology.](https://docs-assets.developer.apple.com/published/5e9a8c09769ff9a0bb500ae84bb9df3c/media-3004318%402x.png)

For information about the keys that you can include in your `Info.plist` file, see [`Information Property List Key Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009247).

##### Code Structure of a Uikit App

UIKit provides many of your app’s core objects, including those that interact with the system, run the app’s main event loop, and display your content onscreen. You use most of these objects as-is or with only minor modifications. Knowing which objects to modify, and when to modify them, is crucial to implementing your app.

The structure of UIKit apps is based on the Model-View-Controller (MVC) design pattern, wherein objects are divided by their purpose. Model objects manage the app’s data and business logic. View objects provide the visual representation of your data. Controller objects act as a bridge between your model and view objects, moving data between them at appropriate times.

The following image represents a fairly typical structure of a UIKit app. You provide the model objects that represent your app’s data structures. UIKit provides most of the view objects, although you can define custom views for your data, as needed. Coordinating the exchange of data between your data objects and the UIKit views are your view controllers and app delegate object.

![An app contains a main app controller and one or more view controllers. It also includes model objects representing the app’s data, and it contains window and view objects for the app’s interface.](https://docs-assets.developer.apple.com/published/b3f961941b323623285121380df8dbad/media-3004320%402x.png)

The UIKit and Foundation frameworks provide many of the basic types that you use to define your app’s model objects. UIKit provides a [`UIDocument`](uidocument.md) object for organizing the data structures that belong in a disk-based file. The Foundation framework defines basic objects representing strings, numbers, arrays, and other data types. The [`Swift Standard Library`](https://developer.apple.com/documentation/Swift/swift-standard-library) provides many of the same types available in the Foundation framework.

UIKit provides most of the objects in the controller and view layers of your app. Specifically, UIKit defines the [`UIView`](uiview.md) class, which is usually responsible for displaying your content onscreen. (You can also render content directly to the screen using Metal and other system frameworks.) The [`UIApplication`](uiapplication.md) object runs your app’s main event loop and manages your app’s overall life cycle.

## See Also

- [UIKit updates](../Updates/UIKit.md)
  Learn about important changes to UIKit.
- [Protecting the User’s Privacy](protecting-the-user-s-privacy.md)
  Secure personal data, and respect user preferences for how data is used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/about-app-development-with-uikit)*