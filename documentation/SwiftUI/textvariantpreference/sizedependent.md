# sizeDependent

**Framework**: SwiftUI  
**Kind**: property

The size dependent preference allows the text to take the available space into account when choosing the size variant to display.

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
static var sizeDependent: SizeDependentTextVariant { get }
```

#### Discussion

When a [`Text`](text.md) provides different size options for its content, the size dependent preference chooses the largest option that fits into the available space without truncating or clipping its content.

> **Note**: Only use this option where needed as it incurrs a performance cost on every [`Text`](text.md) it is applied to, even if the concrete text initializer cannot provide multiple size variants and there is no visual impact.

Only use this option where needed as it incurrs a performance cost on every [`Text`](text.md) it is applied to, even if the concrete text initializer cannot provide multiple size variants and there is no visual impact.

#### Difference to Doccomappleswiftuidocumentationswiftuiviewthatfits

The [`sizeDependent`](textvariantpreference/sizedependent.md) text variant preference differs from [`ViewThatFits`](viewthatfits.md) both in usage and in behavior. [`ViewThatFits`](viewthatfits.md) chooses the first child where the  size fits the available space. For [`Text`](text.md) this means that it will only choose texts that can fit their contents into the available space . With this text variant preference, on the other hand, the largest variant is chosen that can fit the available space while respecting all the regular layout rules, such as [`lineLimit`](environmentvalues/linelimit.md).

To use [`ViewThatFits`](viewthatfits.md), multiple different views have to be provided as the different size options. With this text variant preference, a single [`Text`](text.md) provides the different size variants intrinsicly. The way it generates these size variants and how many size variants are available depends on the text initializer used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textvariantpreference/sizedependent)*