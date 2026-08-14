# init(request:scale:transaction:content:)

**Framework**: SwiftUI  
**Kind**: init

Loads and displays a modifiable image from the specified URL load request in phases.

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
init(request: URLRequest?, scale: CGFloat = 1, transaction: Transaction = Transaction(), @ContentBuilder content: @escaping (AsyncImagePhase) -> Content)
```

#### Discussion

If you set the asynchronous image’s [`URLRequest`](https://developer.apple.com/documentation/foundation/urlrequest) to `nil`, or after you set the request to a value but before the load operation completes, the phase is [`AsyncImagePhase.empty`](asyncimagephase/empty.md). After the operation completes, the phase becomes either [`AsyncImagePhase.failure(_:)`](asyncimagephase/failure(_:).md) or [`AsyncImagePhase.success(_:)`](asyncimagephase/success(_:).md). In the first case, the phase’s [`error`](asyncimagephase/error.md) value indicates the reason for failure. In the second case, the phase’s [`image`](asyncimagephase/image.md) property contains the loaded image. Use the phase to drive the output of the `content` closure, which defines the view’s appearance:

```swift
AsyncImage(request: URLRequest(url: imageURL)) { phase in
    if let image = phase.image {
        image // Displays the loaded image.
    } else if phase.error != nil {
        Color.red // Indicates an error.
    } else {
        Color.blue // Acts as a placeholder.
    }
}
```

To add transitions when you change the [`URLRequest`](https://developer.apple.com/documentation/foundation/urlrequest), apply an identifier to the [`AsyncImage`](asyncimage.md).

You can specify the cache policy and timeout interval via `request`.

## Parameters

- `request`: The [`URLRequest`](https://developer.apple.com/documentation/foundation/urlrequest) of the image to display.
- `scale`: The scale to use for the image. The default is `1`. Set a different value when loading images designed for higher resolution displays. For example, set a value of `2` for an image that you would name with the `@2x` suffix if stored in a file on disk.
- `transaction`: The transaction to use when the phase changes.
- `content`: A closure that takes the load phase as an input, and returns the view to display for the specified phase.

## See Also

- [init(request: URLRequest, scale: CGFloat)](asyncimage/init(request:scale:).md)
  Loads and displays an image from the specified URL load request.
- [init<I, P>(request: URLRequest?, scale: CGFloat, content: (Image) -> I, placeholder: () -> P)](asyncimage/init(request:scale:content:placeholder:).md)
  Loads and displays a modifiable image from the specified URL load request using a custom placeholder until the image loads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/asyncimage/init(request:scale:transaction:content:))*