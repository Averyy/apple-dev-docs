# Xcode library customization

**Framework**: SwiftUI

Expose custom views and modifiers in the Xcode library.

#### Overview

You can add your custom SwiftUI views and view modifiers to Xcode’s library. This allows anyone developing your app or adopting your framework to access them by clicking the Library button (+) in Xcode’s toolbar. You can select and drag the custom library items into code, just like you would for system-provided items.

![None](https://docs-assets.developer.apple.com/published/75621f8df7fbcc9a90dc8e0bf967ef78/xcode-library-customization-hero%402x.png)

To add items to the library, create a structure that conforms to the [`LibraryContentProvider`](https://developer.apple.com/documentation/DeveloperToolsSupport/LibraryContentProvider) protocol and encapsulate any items you want to add as [`LibraryItem`](https://developer.apple.com/documentation/DeveloperToolsSupport/LibraryItem) instances. Implement the doc://com.apple.documentation/documentation/DeveloperToolsSupport/LibraryContentProvider/views-25pdm computed property to add library items containing views. Implement the doc://com.apple.documentation/documentation/DeveloperToolsSupport/LibraryContentProvider/modifiers(base:)-4svii method to add items containing view modifiers. Xcode harvests items from all of the library content providers in your project as you work, and makes them available to you in its library.

## Topics

### Creating library items
- [protocol LibraryContentProvider](../DeveloperToolsSupport/LibraryContentProvider.md)
  A source of Xcode library and code completion content.
- [struct LibraryItem](../DeveloperToolsSupport/LibraryItem.md)
  A single item to add to the Xcode library.

## See Also

- [Previews in Xcode](previews-in-xcode.md)
  Generate dynamic, interactive previews of your custom views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/xcode-library-customization)*