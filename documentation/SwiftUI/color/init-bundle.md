# init(_:bundle:)

**Framework**: SwiftUI  
**Kind**: init

Creates a color from a color set that you indicate by name.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(_ name: String, bundle: Bundle? = nil)
```

#### Discussion

Use this initializer to load a color from a color set stored in an Asset Catalog. The system determines which color within the set to use based on the environment at render time. For example, you can provide light and dark versions for background and foreground colors:

![A screenshot of color sets for foreground and background colors,](https://docs-assets.developer.apple.com/published/8be673759199dc3fa229fc09e8bb0455/Color-init-1%402x.png)

You can then instantiate colors by referencing the names of the assets:

```swift
struct Hello: View {
    var body: some View {
        ZStack {
            Color("background")
            Text("Hello, world!")
                .foregroundStyle(Color("foreground"))
        }
        .frame(width: 200, height: 100)
    }
}
```

SwiftUI renders the appropriate colors for each appearance:

![A side by side comparison of light and dark appearance screenshots](https://docs-assets.developer.apple.com/published/708f550b6b27799d86f6238ac6d65d5e/Color-init-2%402x.png)

## Parameters

- `name`: The name of the color resource to look up.
- `bundle`: The bundle in which to search for the color resource.   If you don’t indicate a bundle, the initializer looks in your app’s   main bundle by default.

## See Also

- [init(_:)](color/init(_:).md)
  Creates a constant color with the values specified by the resolved color.
- [func resolve(in: EnvironmentValues) -> Color.Resolved](color/resolve(in:).md)
  Evaluates this color to a resolved color given the current `context`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color/init(_:bundle:))*