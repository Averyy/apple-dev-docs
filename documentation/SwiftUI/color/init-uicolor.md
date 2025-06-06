# init(uiColor:)

**Framework**: SwiftUI  
**Kind**: init

Creates a color from a UIKit color.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init(uiColor: UIColor)
```

#### Discussion

Use this method to create a SwiftUI color from a [`UIColor`](https://developer.apple.com/documentation/UIKit/UIColor) instance. The new color preserves the adaptability of the original. For example, you can create a rectangle using [`link`](https://developer.apple.com/documentation/UIKit/UIColor/link) to see how the shade adjusts to match the user’s system settings:

```swift
struct Box: View {
    var body: some View {
        Color(uiColor: .link)
            .frame(width: 200, height: 100)
    }
}
```

The `Box` view defined above automatically changes its appearance when the user turns on Dark Mode. With the light and dark appearances placed side by side, you can see the subtle difference in shades:

![A side by side comparison of light and dark appearance screenshots of](https://docs-assets.developer.apple.com/published/599bf4a06d3976ad099cbd7337fdc258/Color-init-3%402x.png)

> **Note**: Use this initializer only if you need to convert an existing [`UIColor`](https://developer.apple.com/documentation/UIKit/UIColor) to a SwiftUI color. Otherwise, create a SwiftUI [`Color`](color.md) using an initializer like [`init(_:red:green:blue:opacity:)`](color/init(_:red:green:blue:opacity:).md), or use a system color like [`blue`](shapestyle/blue.md).

Use this initializer only if you need to convert an existing [`UIColor`](https://developer.apple.com/documentation/UIKit/UIColor) to a SwiftUI color. Otherwise, create a SwiftUI [`Color`](color.md) using an initializer like [`init(_:red:green:blue:opacity:)`](color/init(_:red:green:blue:opacity:).md), or use a system color like [`blue`](shapestyle/blue.md).

## See Also

- [init(nsColor: NSColor)](color/init(nscolor:).md)
  Creates a color from an AppKit color.
- [init(cgColor: CGColor)](color/init(cgcolor:).md)
  Creates a color from a Core Graphics color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color/init(uicolor:))*