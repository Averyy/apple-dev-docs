# ScrollViewReader

**Framework**: SwiftUI  
**Kind**: struct

A view that provides programmatic scrolling, by working with a proxy to scroll to known child views.

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
@frozen
struct ScrollViewReader<Content> where Content : View
```

#### Overview

The scroll view reader’s content view builder receives a [`ScrollViewProxy`](scrollviewproxy.md) instance; you use the proxy’s [`scrollTo(_:anchor:)`](scrollviewproxy/scrollto(_:anchor:).md) to perform scrolling.

The following example creates a [`ScrollView`](scrollview.md) containing 100 views that together display a color gradient. It also contains two buttons, one each at the top and bottom. The top button tells the [`ScrollViewProxy`](scrollviewproxy.md) to scroll to the bottom button, and vice versa.

```swift
@Namespace var topID
@Namespace var bottomID

var body: some View {
    ScrollViewReader { proxy in
        ScrollView {
            Button("Scroll to Bottom") {
                withAnimation {
                    proxy.scrollTo(bottomID)
                }
            }
            .id(topID)

            VStack(spacing: 0) {
                ForEach(0..<100) { i in
                    color(fraction: Double(i) / 100)
                        .frame(height: 32)
                }
            }

            Button("Top") {
                withAnimation {
                    proxy.scrollTo(topID)
                }
            }
            .id(bottomID)
        }
    }
}

func color(fraction: Double) -> Color {
    Color(red: fraction, green: 1 - fraction, blue: 0.5)
}
```

![A scroll view, with a button labeled “Scroll to Bottom” at top.](https://docs-assets.developer.apple.com/published/8735b201580f404d498324837faf9233/SwiftUI-ScrollViewReader-scroll-to-bottom-button%402x.png)

> ❗ **Important**: You may not use the [`ScrollViewProxy`](scrollviewproxy.md) during execution of the `content` view builder; doing so results in a runtime error. Instead, only actions created within `content` can call the proxy, such as gesture handlers or a view’s `onChange(of:perform:)` method.

You may not use the [`ScrollViewProxy`](scrollviewproxy.md) during execution of the `content` view builder; doing so results in a runtime error. Instead, only actions created within `content` can call the proxy, such as gesture handlers or a view’s `onChange(of:perform:)` method.

## Topics

### Creating a scroll view reader
- [init(content: (ScrollViewProxy) -> Content)](scrollviewreader/init(content:).md)
  Creates an instance that can perform programmatic scrolling of its child scroll views.
### Configuring a scroll view reader
- [var content: (ScrollViewProxy) -> Content](scrollviewreader/content.md)
  The view builder that creates the reader’s content.

## Relationships

### Conforms To
- [View](view.md)

## See Also

- [struct ScrollView](scrollview.md)
  A scrollable view.
- [struct ScrollViewProxy](scrollviewproxy.md)
  A proxy value that supports programmatic scrolling of the scrollable views within a view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrollviewreader)*