# cardSnippet

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A container background placement for a card snippet, the card shown for an app entity snippet or a snippet-intent result.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
static let cardSnippet: ContainerBackgroundPlacement
```

## Discussion

This placement applies only to the card snippet shape.

Declare the card’s background with the view’s [`containerBackground(_:for:)`](../view/containerbackground%28_,for%29.md) modifier. The modifier tells the system to draw the background separately from the snippet’s content. For example, the system can animate the snippet’s size smoothly, or replace the background with one that matches the snippet’s parent view.

```swift
MySnippetView()
    .containerBackground(Color.blue.gradient, for: .cardSnippet)
```

Declaring a background is optional. A snippet has a background, so if you don’t declare one, the system draws a default. To opt out of the default, declare a clear background, but only when your design calls for it because the content has to stand on its own.

If a snippet appears somewhere that has no snippet container, such as in your own app’s views, the placement has no effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/containerbackgroundplacement/cardsnippet)*