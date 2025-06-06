# init(url:scale:)

**Framework**: SwiftUI  
**Kind**: init

Loads and displays an image from the specified URL.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init(url: URL?, scale: CGFloat = 1) where Content == Image
```

#### Discussion

Until the image loads, SwiftUI displays a default placeholder. When the load operation completes successfully, SwiftUI updates the view to show the loaded image. If the operation fails, SwiftUI continues to display the placeholder. The following example loads and displays an icon from an example server:

```swift
AsyncImage(url: URL(string: "https://example.com/icon.png"))
```

If you want to customize the placeholder or apply image-specific modifiers — like [`resizable(capInsets:resizingMode:)`](image/resizable(capinsets:resizingmode:).md) — to the loaded image, use the [`init(url:scale:content:placeholder:)`](asyncimage/init(url:scale:content:placeholder:).md) initializer instead.

## Parameters

- `url`: The URL of the image to display.
- `scale`: The scale to use for the image. The default is  . Set a   different value when loading images designed for higher resolution   displays. For example, set a value of   for an image that you   would name with the   suffix if stored in a file on disk.

## See Also

- [init<I, P>(url: URL?, scale: CGFloat, content: (Image) -> I, placeholder: () -> P)](asyncimage/init(url:scale:content:placeholder:).md)
  Loads and displays a modifiable image from the specified URL using a custom placeholder until the image loads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/asyncimage/init(url:scale:))*