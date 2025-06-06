# textVariant(_:)

**Framework**: SwiftUI  
**Kind**: method

Controls the way text size variants are chosen.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func textVariant<V>(_ preference: V) -> some View where V : TextVariantPreference
```

#### Discussion

Certain types of text, such as `Text(_:format:)`, can generate strings of different size to better fit the available space. By default, all text uses the widest available variant. Setting the variant to be [`sizeDependent`](textvariantpreference/sizedependent.md) allows the text to take the available space into account when choosing what content to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/textvariant(_:))*