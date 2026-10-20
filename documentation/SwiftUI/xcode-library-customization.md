# Xcode library customization

**Framework**: SwiftUI

Expose custom views and modifiers in the Xcode library.

#### Overview

You can add your custom SwiftUI views and view modifiers to Xcode’s library. This allows anyone developing your app or adopting your framework to access them by clicking the Library button (+) in Xcode’s toolbar. You can select and drag the custom library items into code, just like you would for system-provided items.

![](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/xcode-library-customization-hero@2x.png)

To add items to the library, create a structure that conforms to the [`LibraryContentProvider`](../DeveloperToolsSupport/librarycontentprovider.md) protocol and encapsulate any items you want to add as [`LibraryItem`](../DeveloperToolsSupport/libraryitem.md) instances. Implement the [`views`](../DeveloperToolsSupport/librarycontentprovider/views.md) computed property to add library items containing views. Implement the [`modifiers(base:)`](../DeveloperToolsSupport/librarycontentprovider/modifiers%28base%29.md) method to add items containing view modifiers. Xcode harvests items from all of the library content providers in your project as you work, and makes them available to you in its library.

## Topics

### Creating library items
- [protocol LibraryContentProvider](../DeveloperToolsSupport/librarycontentprovider.md)
  A source of Xcode library and code completion content.
- [struct LibraryItem](../DeveloperToolsSupport/libraryitem.md)
  A single item to add to the Xcode library.

## See Also

### Tool support
- [Previews in Xcode](./previews-in-xcode.md)
  Generate dynamic, interactive previews of your custom views.
- [Performance analysis](./performance-analysis.md)
  Measure and improve your app’s responsiveness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/xcode-library-customization)*