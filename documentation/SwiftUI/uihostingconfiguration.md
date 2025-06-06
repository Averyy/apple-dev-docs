# UIHostingConfiguration

**Framework**: SwiftUI  
**Kind**: struct

A content configuration suitable for hosting a hierarchy of SwiftUI views.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct UIHostingConfiguration<Content, Background> where Content : View, Background : View
```

#### Overview

Use a value of this type, which conforms to the [`UIContentConfiguration`](https://developer.apple.com/documentation/UIKit/UIContentConfiguration-9eib5) protocol, with a [`UICollectionViewCell`](https://developer.apple.com/documentation/UIKit/UICollectionViewCell) or [`UITableViewCell`](https://developer.apple.com/documentation/UIKit/UITableViewCell) to host a hierarchy of SwiftUI views in a collection or table view, respectively. For example, the following shows a stack with an image and text inside the cell:

```swift
myCell.contentConfiguration = UIHostingConfiguration {
    HStack {
        Image(systemName: "star").foregroundStyle(.purple)
        Text("Favorites")
        Spacer()
    }
}
```

You can also customize the background of the containing cell. The following example draws a blue background:

```swift
myCell.contentConfiguration = UIHostingConfiguration {
    HStack {
        Image(systemName: "star").foregroundStyle(.purple)
        Text("Favorites")
        Spacer()
    }
}
.background {
    Color.blue
}
```

When used in a list layout, certain APIs are bridged automatically, like swipe actions and separator alignment. The following example shows a trailing yellow star swipe action:

```swift
cell.contentConfiguration = UIHostingConfiguration {
    HStack {
        Image(systemName: "airplane")
        Text("Flight 123")
        Spacer()
    }
    .swipeActions {
        Button { ... } label: {
            Label("Favorite", systemImage: "star")
        }
        .tint(.yellow)
    }
}
```

## Topics

### Creating and updating a configuration
- [init(content: () -> Content)](uihostingconfiguration/init(content:).md)
  Creates a hosting configuration with the given contents.
### Setting the background
- [func background<S>(S) -> UIHostingConfiguration<Content, _UIHostingConfigurationBackgroundView<S>>](uihostingconfiguration/background(_:).md)
  Sets the background contents for the hosting configuration’s enclosing cell.
- [func background<B>(content: () -> B) -> UIHostingConfiguration<Content, B>](uihostingconfiguration/background(content:).md)
  Sets the background contents for the hosting configuration’s enclosing cell.
### Setting margins
- [func margins(_:_:)](uihostingconfiguration/margins(_:_:).md)
  Sets the margins around the content of the configuration.
### Setting a size
- [func minSize(width: CGFloat?, height: CGFloat?) -> UIHostingConfiguration<Content, Background>](uihostingconfiguration/minsize(width:height:).md)
  Sets the minimum size for the configuration.
- [func minSize() -> UIHostingConfiguration<Content, Background>](uihostingconfiguration/minsize.md)
  Sets the minimum size for the configuration.

## Relationships

### Conforms To
- [UIContentConfiguration](../UIKit/UIContentConfiguration-9eib5.md)

## See Also

- [Using SwiftUI with UIKit](../UIKit/using-swiftui-with-uikit.md)
  Learn how to incorporate SwiftUI views into a UIKit app.
- [Unifying your app’s animations](unifying-your-app-s-animations.md)
  Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.
- [class UIHostingController](uihostingcontroller.md)
  A UIKit view controller that manages a SwiftUI view hierarchy.
- [struct UIHostingControllerSizingOptions](uihostingcontrollersizingoptions.md)
  Options for how a hosting controller tracks its content’s size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uihostingconfiguration)*