# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a custom font from a platform font instance.

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
init(_ font: CTFont)
```

## Discussion

Initializing [`Font`](../font.md) with platform font instance ([`CTFont`](../../CoreText/ctfont.md)) can bridge SwiftUI [`Font`](../font.md) with [`NSFont`](../../AppKit/nsfont.md) or [`UIFont`](../../UIKit/uifont.md), both of which are toll-free bridged to [`CTFont`](../../CoreText/ctfont.md). For example:

```swift
// Use native Core Text API to create desired ctFont.
let ctFont = CTFontCreateUIFontForLanguage(.system, 12, nil)!

// Create SwiftUI Text with the CTFont instance.
let text = Text("Hello").font(Font(ctFont))
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/font/init(_:))*