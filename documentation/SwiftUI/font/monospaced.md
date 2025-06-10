# monospaced(_:)

**Framework**: SwiftUI  
**Kind**: method

Returns a font adding or removing fixed-width design from the same family as the base font.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func monospaced(_ isActive: Bool) -> Font
```

#### Return Value

A font with the fixed-width design added or removed, from the same family as the base font, if one is available, and a default font otherwise.

#### Discussion

If there’s no suitable font face in the same family, SwiftUI returns a default font.

The following example adds the `monospaced()` modifier to the default system font, then applies this font to a [`Text`](text.md) view:

```swift
struct ContentView: View {
    let myFont = Font
        .system(size: 24)
        .monospaced(true)

    var body: some View {
        Text("Hello, world!")
            .font(myFont)
            .padding()
            .navigationTitle("Monospaced")
    }
}
```

![A macOS window showing the text Hello, world in a 24-point](https://docs-assets.developer.apple.com/published/fe6495d1d5d860442569b8e417b11198/Environment-Font-monospaced-1%402x.png)

SwiftUI may provide different fixed-width replacements for standard user interface fonts (such as [`title`](font/title.md), or a system font created with [`system(_:design:)`](font/system(_:design:).md)) than for those same fonts when created by name with [`custom(_:size:)`](font/custom(_:size:).md).

The [`font(_:)`](view/font(_:).md) modifier applies the font to all text within the view. To mix fixed-width text with other styles in the same `Text` view, use the [`init(_:)`](text/init(_:)-1a4oh.md) initializer to use an appropriately-styled [`AttributedString`](https://developer.apple.com/documentation/Foundation/AttributedString) for the text view’s content. You can use the [`init(markdown:options:baseURL:)`](https://developer.apple.com/documentation/Foundation/AttributedString/init(markdown:options:baseURL:)-52n3u) initializer to provide a Markdown-formatted string containing the backtick-syntax (`…`) to apply code voice to specific ranges of the attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/font/monospaced(_:))*