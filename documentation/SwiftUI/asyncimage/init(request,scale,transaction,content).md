# init(request:scale:transaction:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Loads and displays a modifiable image from the specified URL load request in phases.

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
init(request: URLRequest?, scale: CGFloat = 1, transaction: Transaction = Transaction(), @ContentBuilder content: @escaping (AsyncImagePhase) -> Content)
```

#### Discussion

If you set the asynchronous image’s [`URLRequest`](../../Foundation/urlrequest.md) to `nil`, or after you set the request to a value but before the load operation completes, the phase is [`AsyncImagePhase.empty`](../asyncimagephase/empty.md). After the operation completes, the phase becomes either [`AsyncImagePhase.failure(_:)`](../asyncimagephase/failure%28_%29.md) or [`AsyncImagePhase.success(_:)`](../asyncimagephase/success%28_%29.md). In the first case, the phase’s [`error`](../asyncimagephase/error.md) value indicates the reason for failure. In the second case, the phase’s [`image`](../asyncimagephase/image.md) property contains the loaded image. Use the phase to drive the output of the `content` closure, which defines the view’s appearance:

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

To add transitions when you change the [`URLRequest`](../../Foundation/urlrequest.md), apply an identifier to the [`AsyncImage`](../asyncimage.md).

You can specify the cache policy and timeout interval via `request`.

## Parameters

- `request`: The [`URLRequest`](../../Foundation/urlrequest.md) of the image to display.
- `scale`: The scale to use for the image. The default is `1`. Set a different value when loading images designed for higher resolution displays. For example, set a value of `2` for an image that you would name with the `@2x` suffix if stored in a file on disk.
- `transaction`: The transaction to use when the phase changes.
- `content`: A closure that takes the load phase as an input, and returns the view to display for the specified phase.

## See Also

### Loading an image with a URL request
- [init(request: URLRequest, scale: CGFloat)](./init%28request,scale%29.md)
  Loads and displays an image from the specified URL load request.
- [init<I, P>(request: URLRequest?, scale: CGFloat, content: (Image) -> I, placeholder: () -> P)](./init%28request,scale,content,placeholder%29.md)
  Loads and displays a modifiable image from the specified URL load request using a custom placeholder until the image loads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/asyncimage/init(request:scale:transaction:content:))*