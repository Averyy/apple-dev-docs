# init(uiColor:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

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

## Discussion

Use this method to create a SwiftUI color from a [`UIColor`](../../UIKit/uicolor.md) instance. The new color preserves the adaptability of the original. For example, you can create a rectangle using [`link`](../../UIKit/uicolor/link.md) to see how the shade adjusts to match the user’s system settings:

```swift
struct Box: View {
    var body: some View {
        Color(uiColor: .link)
            .frame(width: 200, height: 100)
    }
}
```

The `Box` view defined above automatically changes its appearance when the user turns on Dark Mode. With the light and dark appearances placed side by side, you can see the subtle difference in shades:

![A side by side comparison of light and dark appearance screenshots of](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/Color-init-3@2x.png)

> **Note**: Use this initializer only if you need to convert an existing [`UIColor`](../../UIKit/uicolor.md) to a SwiftUI color. Otherwise, create a SwiftUI [`Color`](../color.md) using an initializer like [`init(_:red:green:blue:opacity:)`](./init%28_,red,green,blue,opacity%29.md), or use a system color like [`blue`](../shapestyle/blue.md).

## Parameters

- `uiColor`: A [`UIColor`](../../UIKit/uicolor.md) instance from which to create a color.

## See Also

### Creating a color from another color
- [init(nsColor: NSColor)](./init%28nscolor%29.md)
  Creates a color from an AppKit color.
- [init(cgColor: CGColor)](./init%28cgcolor%29.md)
  Creates a color from a Core Graphics color.
- [var cgColor: CGColor?](./cgcolor.md)
  A Core Graphics representation of the color, if available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color/init(uicolor:))*