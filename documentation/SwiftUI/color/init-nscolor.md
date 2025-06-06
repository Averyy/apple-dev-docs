# init(nsColor:)

**Framework**: SwiftUI  
**Kind**: init

Creates a color from an AppKit color.

**Availability**:
- macOS 12.0+

## Declaration

```swift
nonisolated
init(nsColor: NSColor)
```

#### Discussion

Use this method to create a SwiftUI color from an [`NSColor`](https://developer.apple.com/documentation/AppKit/NSColor) instance. The new color preserves the adaptability of the original. For example, you can create a rectangle using [`linkColor`](https://developer.apple.com/documentation/AppKit/NSColor/linkColor) to see how the shade adjusts to match the user’s system settings:

```swift
struct Box: View {
    var body: some View {
        Color(nsColor: .linkColor)
            .frame(width: 200, height: 100)
    }
}
```

The `Box` view defined above automatically changes its appearance when the user turns on Dark Mode. With the light and dark appearances placed side by side, you can see the subtle difference in shades:

![A side by side comparison of light and dark appearance screenshots of](https://docs-assets.developer.apple.com/published/5d1b72a6328b7881b1e9304e8b0bc496/Color-init-4%402x.png)

> **Note**: Use this initializer only if you need to convert an existing [`NSColor`](https://developer.apple.com/documentation/AppKit/NSColor) to a SwiftUI color. Otherwise, create a SwiftUI [`Color`](color.md) using an initializer like [`init(_:red:green:blue:opacity:)`](color/init(_:red:green:blue:opacity:).md), or use a system color like [`blue`](shapestyle/blue.md).

Use this initializer only if you need to convert an existing [`NSColor`](https://developer.apple.com/documentation/AppKit/NSColor) to a SwiftUI color. Otherwise, create a SwiftUI [`Color`](color.md) using an initializer like [`init(_:red:green:blue:opacity:)`](color/init(_:red:green:blue:opacity:).md), or use a system color like [`blue`](shapestyle/blue.md).

## See Also

- [init(uiColor: UIColor)](color/init(uicolor:).md)
  Creates a color from a UIKit color.
- [init(cgColor: CGColor)](color/init(cgcolor:).md)
  Creates a color from a Core Graphics color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color/init(nscolor:))*