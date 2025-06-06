# init(url:scale:transaction:content:)

**Framework**: SwiftUI  
**Kind**: init

Loads and displays a modifiable image from the specified URL in phases.

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
init(url: URL?, scale: CGFloat = 1, transaction: Transaction = Transaction(), @ViewBuilder content: @escaping (AsyncImagePhase) -> Content)
```

#### Discussion

If you set the asynchronous image’s URL to `nil`, or after you set the URL to a value but before the load operation completes, the phase is [`AsyncImagePhase.empty`](asyncimagephase/empty.md). After the operation completes, the phase becomes either [`AsyncImagePhase.failure(_:)`](asyncimagephase/failure(_:).md) or [`AsyncImagePhase.success(_:)`](asyncimagephase/success(_:).md). In the first case, the phase’s [`error`](asyncimagephase/error.md) value indicates the reason for failure. In the second case, the phase’s [`image`](asyncimagephase/image.md) property contains the loaded image. Use the phase to drive the output of the `content` closure, which defines the view’s appearance:

```swift
AsyncImage(url: URL(string: "https://example.com/icon.png")) { phase in
    if let image = phase.image {
        image // Displays the loaded image.
    } else if phase.error != nil {
        Color.red // Indicates an error.
    } else {
        Color.blue // Acts as a placeholder.
    }
}
```

To add transitions when you change the URL, apply an identifier to the [`AsyncImage`](asyncimage.md).

## Parameters

- `url`: The URL of the image to display.
- `scale`: The scale to use for the image. The default is  . Set a   different value when loading images designed for higher resolution   displays. For example, set a value of   for an image that you   would name with the   suffix if stored in a file on disk.
- `transaction`: The transaction to use when the phase changes.
- `content`: A closure that takes the load phase as an input, and   returns the view to display for the specified phase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/asyncimage/init(url:scale:transaction:content:))*