# default

**Framework**: SwiftUI  
**Kind**: property

The default strategy based on the context it is used in.

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
static let `default`: Text.AlignmentStrategy
```

#### Discussion

The default strategy for [`Text`](text.md) is [`layoutBased`](text/alignmentstrategy/layoutbased.md). UI components that accept user input, such as [`TextEditor`](texteditor.md) and [`TextField`](textfield.md), default to [`writingDirectionBased`](text/alignmentstrategy/writingdirectionbased.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/alignmentstrategy/default)*