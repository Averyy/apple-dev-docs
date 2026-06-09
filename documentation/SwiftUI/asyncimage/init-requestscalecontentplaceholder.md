# init(request:scale:content:placeholder:)

**Framework**: SwiftUI  
**Kind**: init

Loads and displays a modifiable image from the specified URL load request using a custom placeholder until the image loads.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
init<I, P>(request: URLRequest?, scale: CGFloat = 1, @ContentBuilder content: @escaping (Image) -> I, @ContentBuilder placeholder: @escaping () -> P) where Content == _AsyncImageConditionalContent<I, P>, I : View, P : View
```

#### Discussion

Until the image loads, SwiftUI displays the placeholder view that you specify. When the load operation completes successfully, SwiftUI updates the view to show content that you specify, which you create using the loaded image. For example, you can show a green placeholder, followed by a tiled version of the loaded image:

```swift
AsyncImage(request: URLRequest(url: imageURL)) { image in
    image.resizable(resizingMode: .tile)
} placeholder: {
    Color.green
}
```

If the load operation fails, SwiftUI continues to display the placeholder. To be able to display a different view on a load error, use the [`init(url:scale:transaction:content:)`](asyncimage/init(url:scale:transaction:content:).md) initializer instead.

## Parameters

- `request`: The [`URLRequest`](https://developer.apple.com/documentation/Foundation/URLRequest) of the image to display.
- `scale`: The scale to use for the image. The default is `1`. Set a different value when loading images designed for higher resolution displays. For example, set a value of `2` for an image that you would name with the `@2x` suffix if stored in a file on disk.
- `content`: A closure that takes the loaded image as an input, and returns the view to show. You can return the image directly, or modify it as needed before returning it.
- `placeholder`: A closure that returns the view to show until the load operation completes successfully.

## See Also

- [init(request: URLRequest, scale: CGFloat)](asyncimage/init(request:scale:).md)
  Loads and displays an image from the specified URL load request.
- [init(request: URLRequest?, scale: CGFloat, transaction: Transaction, content: (AsyncImagePhase) -> Content)](asyncimage/init(request:scale:transaction:content:).md)
  Loads and displays a modifiable image from the specified URL load request in phases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/asyncimage/init(request:scale:content:placeholder:))*