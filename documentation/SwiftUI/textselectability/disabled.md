# disabled

**Framework**: SwiftUI  
**Kind**: property

A selectability value that disables text selection by the person using your app.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
static var disabled: DisabledTextSelectability { get }
```

#### Discussion

Use this property to disable text selection of views that you don’t want people to select and copy, even if contained within an overall context that allows text selection.

```swift
content // Content that might contain Text views.
   .textSelection(.disabled)
   .padding()
   .contentShape(Rectangle())
   .gesture(someGesture)
```

## See Also

- [static var enabled: EnabledTextSelectability](textselectability/enabled.md)
  A selectability value that enables text selection by a person using your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textselectability/disabled)*