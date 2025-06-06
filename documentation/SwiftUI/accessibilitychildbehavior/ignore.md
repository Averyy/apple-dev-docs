# ignore

**Framework**: Swiftui  
**Kind**: property

Any child accessibility elements become hidden.

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
static let ignore: AccessibilityChildBehavior
```

#### Discussion

Use this behavior when you want a view represented by a single accessibility element. The new accessibility element has no initial properties. So you will need to use other accessibility modifiers, such as [`accessibilityLabel(_:)`](view/accessibilitylabel(_:).md), to begin making it accessible.

```swift
var body: some View {
    VStack {
        Button("Previous Page", action: goBack)
        Text("\(pageNumber)")
        Button("Next Page", action: goForward)
    }
    .accessibilityElement(children: .ignore)
    .accessibilityValue("Page \(pageNumber) of \(pages.count)")
    .accessibilityAdjustableAction { action in
        if action == .increment {
            goForward()
        } else {
            goBack()
        }
    }
}
```

Before using the  [`ignore`](accessibilitychildbehavior/ignore.md)behavior, consider using the [`combine`](accessibilitychildbehavior/combine.md) behavior.

> **Note**: A new accessibility element is always created.

## See Also

- [static let combine: AccessibilityChildBehavior](accessibilitychildbehavior/combine.md)
  Any child accessibility element’s properties are merged into the new accessibility element.
- [static let contain: AccessibilityChildBehavior](accessibilitychildbehavior/contain.md)
  Any child accessibility elements become children of the new accessibility element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/SwiftUI/accessibilitychildbehavior/ignore)*