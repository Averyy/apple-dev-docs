# Link

**Framework**: SwiftUI  
**Kind**: struct

A control for navigating to a URL.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@MainActor
@preconcurrency struct Link<Label> where Label : View
```

#### Overview

Create a link by providing a destination URL and a title. The title tells the user the purpose of the link, and can be a string, a title key that produces a localized string, or a view that acts as a label. The example below creates a link to `example.com` and displays the title string as a link-styled view:

```swift
Link("View Our Terms of Service",
      destination: URL(string: "https://www.example.com/TOS.html")!)
```

When a user taps or clicks a `Link`, the default behavior depends on the contents of the URL. For example, SwiftUI opens a Universal Link in the associated app if possible, or in the user’s default web browser if not. Alternatively, you can override the default behavior by setting the [`openURL`](environmentvalues/openurl.md) environment value with a custom [`OpenURLAction`](openurlaction.md):

```swift
Link("Visit Our Site", destination: URL(string: "https://www.example.com")!)
    .environment(\.openURL, OpenURLAction { url in
        print("Open \(url)")
        return .handled
    })
```

As with other views, you can style links using standard view modifiers depending on the view type of the link’s label. For example, a [`Text`](text.md) label could be modified with a custom [`font(_:)`](view/font(_:).md) or [`foregroundColor(_:)`](view/foregroundcolor(_:).md) to customize the appearance of the link in your app’s UI.

## Topics

### Creating a link
- [init(_:destination:)](link/init(_:destination:).md)
  Creates a control, consisting of a URL and a title key, used to navigate to a URL.
- [init(destination: URL, label: () -> Label)](link/init(destination:label:).md)
  Creates a control, consisting of a URL and a label, used to navigate to the given URL.

## Relationships

### Conforms To
- [View](view.md)

## See Also

- [struct ShareLink](sharelink.md)
  A view that controls a sharing presentation.
- [struct SharePreview](sharepreview.md)
  A representation of a type to display in a share preview.
- [struct TextFieldLink](textfieldlink.md)
  A control that requests text input from the user when pressed.
- [struct HelpLink](helplink.md)
  A button with a standard appearance that opens app-specific help documentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/link)*