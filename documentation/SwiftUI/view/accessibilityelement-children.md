# accessibilityElement(children:)

**Framework**: SwiftUI  
**Kind**: method

Creates a new accessibility element, or modifies the [`AccessibilityChildBehavior`](accessibilitychildbehavior.md) of the existing accessibility element.

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
func accessibilityElement(children: AccessibilityChildBehavior = .ignore) -> some View
```

#### Discussion

See also:

- [`ignore`](accessibilitychildbehavior/ignore.md)
- [`combine`](accessibilitychildbehavior/combine.md)
- [`contain`](accessibilitychildbehavior/contain.md)

## Parameters

- `children`: The behavior to use when creating or   transforming an accessibility element.   The default is 

## See Also

- [func accessibilityChildren<V>(children: () -> V) -> some View](view/accessibilitychildren(children:).md)
  Replaces the existing accessibility element’s children with one or more new synthetic accessibility elements.
- [func accessibilityRepresentation<V>(representation: () -> V) -> some View](view/accessibilityrepresentation(representation:).md)
  Replaces one or more accessibility elements for this view with new accessibility elements.
- [struct AccessibilityChildBehavior](accessibilitychildbehavior.md)
  Defines the behavior for the child elements of the new parent element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/accessibilityelement(children:))*