# foregroundColor(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the color of the text displayed by this view.

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
nonisolated
func foregroundColor(_ color: Color?) -> Text
```

#### Return Value

A text view that uses the color value you supply.

#### Discussion

Use this method to change the color of the text rendered by a text view.

For example, you can display the names of the colors red, green, and blue in their respective colors:

```swift
HStack {
    Text("Red").foregroundColor(.red)
    Text("Green").foregroundColor(.green)
    Text("Blue").foregroundColor(.blue)
}
```

![Three text views arranged horizontally, each containing](https://docs-assets.developer.apple.com/published/31654f673e42a4a453b46dbad7d32b61/SwiftUI-Text-foregroundColor%402x.png)

## Parameters

- `color`: The color to use when displaying this text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/foregroundcolor(_:))*