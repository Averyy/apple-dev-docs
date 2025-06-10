# +(_:_:)

**Framework**: SwiftUI  
**Kind**: op

Concatenates the text in two text views in a new text view.

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
static func + (lhs: Text, rhs: Text) -> Text
```

#### Return Value

A new text view containing the combined contents of the two input text views.

#### Discussion

> **Note**:  The `+` on `Text` has been deprecated. Using this operator to concatenate texts hardcodes a specific order for part of the sentence. This may lead to incorrect localization, especially for right-to-left languages. Instead, prefer using the initializer on `Text` that allows for string interpolation. For example, instead of `Text("Hello") + Text(name)`, that concatenation can be equivalently expressed as `Text("Hello, \(name)!")`. See [`Text`](text.md) for more information on localization and string interpolation.

## Parameters

- `lhs`: The first text view with text to combine.
- `rhs`: The second text view with text to combine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/+(_:_:))*