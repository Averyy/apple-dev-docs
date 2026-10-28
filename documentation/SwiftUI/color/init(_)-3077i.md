# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a color from an AppKit color.

**Availability**:
- macOS 10.15+ - Deprecated in 27.2

> **Deprecated**: Use [`init(nsColor:)`](./init%28nscolor%29.md) instead.

## Declaration

```swift
nonisolated
init(_ color: NSColor)
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
init(_ color: UIColor)
```

## Discussion

Use this method to create a SwiftUI color from an [`NSColor`](../../AppKit/nscolor.md) instance. The new color preserves the adaptability of the original. For example, you can create a rectangle using [`linkColor`](../../AppKit/nscolor/linkcolor.md) to see how the shade adjusts to match the user’s system settings:

```swift
struct Box: View {
    var body: some View {
        Color(NSColor.linkColor)
            .frame(width: 200, height: 100)
    }
}
```

The `Box` view defined above automatically changes its appearance when the user turns on Dark Mode. With the light and dark appearances placed side by side, you can see the subtle difference in shades:

![A side by side comparison of light and dark appearance screenshots of rectangles rendered with the link color. The light variant appears on the left, and the dark variant on the right.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/Color-init-4@2x.png)

> **Note**: Use this initializer only if you need to convert an existing [`NSColor`](../../AppKit/nscolor.md) to a SwiftUI color. Otherwise, create a SwiftUI [`Color`](../color.md) using an initializer like [`init(_:red:green:blue:opacity:)`](./init%28_,red,green,blue,opacity%29.md), or use a system color like [`blue`](../shapestyle/blue.md).

## Parameters

- `color`: An [`NSColor`](../../AppKit/nscolor.md) instance from which to create a color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color/init(_:)-3077i)*