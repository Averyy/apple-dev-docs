# init(request:scale:)

**Framework**: SwiftUI  
**Kind**: init

Loads and displays an image from the specified URL load request.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
nonisolated
init(request: URLRequest, scale: CGFloat = 1) where Content == Image
```

#### Discussion

Until the image loads, SwiftUI displays a default placeholder. When the load operation completes successfully, SwiftUI updates the view to show the loaded image. If the operation fails, SwiftUI continues to display the placeholder. The following example loads and displays an icon from an example server:

```swift
AsyncImage(request: URLRequest(url: imageURL))
```

If you want to customize the placeholder or apply image-specific modifiers — like [`resizable(capInsets:resizingMode:)`](image/resizable(capinsets:resizingmode:).md) — to the loaded image, use the [`init(request:scale:content:placeholder:)`](asyncimage/init(request:scale:content:placeholder:).md) initializer instead.

## Parameters

- `request`: The [`URLRequest`](https://developer.apple.com/documentation/foundation/urlrequest) of the image to display.
- `scale`: The scale to use for the image. The default is `1`. Set a different value when loading images designed for higher resolution displays. For example, set a value of `2` for an image that you would name with the `@2x` suffix if stored in a file on disk.

## See Also

- [init<I, P>(request: URLRequest?, scale: CGFloat, content: (Image) -> I, placeholder: () -> P)](asyncimage/init(request:scale:content:placeholder:).md)
  Loads and displays a modifiable image from the specified URL load request using a custom placeholder until the image loads.
- [init(request: URLRequest?, scale: CGFloat, transaction: Transaction, content: (AsyncImagePhase) -> Content)](asyncimage/init(request:scale:transaction:content:).md)
  Loads and displays a modifiable image from the specified URL load request in phases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/asyncimage/init(request:scale:))*