# default

**Framework**: SwiftUI  
**Kind**: property

The default strategy based on the context it is used in.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
static let `default`: Text.AlignmentStrategy
```

#### Discussion

The default strategy for [`Text`](text.md) is [`layoutBased`](text/alignmentstrategy/layoutbased.md). UI components that accept user input, such as [`TextEditor`](texteditor.md) and [`TextField`](textfield.md), default to [`writingDirectionBased`](text/alignmentstrategy/writingdirectionbased.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/alignmentstrategy/default)*