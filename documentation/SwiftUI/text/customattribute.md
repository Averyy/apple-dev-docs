# customAttribute(_:)

**Framework**: SwiftUI  
**Kind**: method

Adds a custom attribute to the text view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func customAttribute<T>(_ value: T) -> Text where T : TextAttribute
```

#### Return Value

A version of the text view with `value` attached.

#### Discussion

Only one attribute of each type may be attached to each text view, with inner attributes taking precedence.

## Parameters

- `value`: The attribute to attach.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/customattribute(_:))*