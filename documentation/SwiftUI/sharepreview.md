# SharePreview

**Framework**: SwiftUI  
**Kind**: struct

A representation of a type to display in a share preview.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct SharePreview<Image, Icon> where Image : Transferable, Icon : Transferable
```

## Mentions

- [Configure your apps navigation titles](configure-your-apps-navigation-titles.md)

#### Overview

Use this type when sharing content that the system can’t preview automatically:

```swift
struct Photo: Transferable {
    static var transferRepresentation: some TransferRepresentation {
        ProxyRepresentation(\.image)
    }

    public var image: Image
    public var caption: String
}

struct PhotoView: View {
    let photo: Photo

    var body: View {
        photo.image
            .toolbar {
                ShareLink(
                    item: photo,
                    preview: SharePreview(
                        photo.caption,
                        image: photo.image))
            }
    }
}
```

You can also provide a preview to speed up the sharing process. In the following example the preview appears immediately; if you omit the preview instead, the system fetches the link’s metadata over the network:

```swift
ShareLink(
    item: URL(string: "https://developer.apple.com/xcode/swiftui/")!,
    preview: SharePreview(
        "SwiftUI",
        image: Image("SwiftUI"))
```

You can provide unique previews for each item in a collection of items that a `ShareLink` links to:

```swift
ShareLink(items: photos) { photo in
    SharePreview(photo.caption, image: photo.image)
}
```

The share interface decides how to combine those previews.

Each preview specifies text and images that describe an item of the type. The preview’s `image` parameter is typically a full-size representation of the item. For instance, if the system prepares a preview for a link to a webpage, the image might be the hero image on that webpage.

The preview’s `icon` parameter is typically a thumbnail-sized representation of the source of the item. For instance, if the system prepares a preview for a link to a webpage, the icon might be an image that represents the website overall.

The system may reuse a single preview representation for multiple previews, and show different images in each context. For more information and recommended sizes for each image, see [`TN2444: Best Practices for Link Previews in Messages`](https://developer.apple.comhttps://developer.apple.com/library/archive/technotes/tn2444/_index.html).

## Topics

### Creating a preview
- [init(_:)](sharepreview/init(_:).md)
  Creates a preview representation.
- [init(_:image:)](sharepreview/init(_:image:).md)
  Creates a preview representation.
- [init(_:icon:)](sharepreview/init(_:icon:).md)
  Creates a preview representation.
- [init(_:image:icon:)](sharepreview/init(_:image:icon:).md)
  Creates a preview representation.

## See Also

- [struct Link](link.md)
  A control for navigating to a URL.
- [struct ShareLink](sharelink.md)
  A view that controls a sharing presentation.
- [struct TextFieldLink](textfieldlink.md)
  A control that requests text input from the user when pressed.
- [struct HelpLink](helplink.md)
  A button with a standard appearance that opens app-specific help documentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sharepreview)*