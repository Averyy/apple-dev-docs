# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a color from a UIKit color.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- tvOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 6.0+ - Deprecated in 27.2

> **Deprecated**: Use [`init(uiColor:)`](./init%28uicolor%29.md) instead.

## Declaration

```swift
init(_ color: UIColor)
```

**Other overloads**:

```swift
init(_ resolved: Color.Resolved)
```

```swift
init(_ resolved: Color.ResolvedHDR)
```

```swift
init(_ resource: ColorResource)
```

```swift
init<T>(_ color: T) where T : Hashable, T : ShapeStyle, T.Resolved == Color.Resolved
```

```swift
init<T>(_ color: T) where T : Hashable, T : ShapeStyle, T.Resolved == Color.ResolvedHDR
```

```swift
init(_ cgColor: CGColor)
```

```swift
nonisolated
init(_ color: NSColor)
```

## Discussion

Use this method to create a SwiftUI color from a [`UIColor`](../../UIKit/uicolor.md) instance. The new color preserves the adaptability of the original. For example, you can create a rectangle using [`link`](../../UIKit/uicolor/link.md) to see how the shade adjusts to match the user’s system settings:

```swift
struct Box: View {
    var body: some View {
        Color(UIColor.link)
            .frame(width: 200, height: 100)
    }
}
```

The `Box` view defined above automatically changes its appearance when the user turns on Dark Mode. With the light and dark appearances placed side by side, you can see the subtle difference in shades:

![A side by side comparison of light and dark appearance screenshots of rectangles rendered with the link color. The light variant appears on the left, and the dark variant on the right.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/Color-init-3@2x.png)

> **Note**: Use this initializer only if you need to convert an existing [`UIColor`](../../UIKit/uicolor.md) to a SwiftUI color. Otherwise, create a SwiftUI [`Color`](../color.md) using an initializer like [`init(_:red:green:blue:opacity:)`](./init%28_,red,green,blue,opacity%29.md), or use a system color like [`blue`](../shapestyle/blue.md).

## Parameters

- `color`: A [`UIColor`](../../UIKit/uicolor.md) instance from which to create a color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color/init(_:)-5dwxf)*