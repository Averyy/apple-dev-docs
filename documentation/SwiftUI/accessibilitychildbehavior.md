# AccessibilityChildBehavior

**Framework**: SwiftUI  
**Kind**: struct

Defines the behavior for the child elements of the new parent element.

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
struct AccessibilityChildBehavior
```

## Topics

### Getting behaviors
- [static let combine: AccessibilityChildBehavior](accessibilitychildbehavior/combine.md)
  Any child accessibility element’s properties are merged into the new accessibility element.
- [static let contain: AccessibilityChildBehavior](accessibilitychildbehavior/contain.md)
  Any child accessibility elements become children of the new accessibility element.
- [static let ignore: AccessibilityChildBehavior](accessibilitychildbehavior/ignore.md)
  Any child accessibility elements become hidden.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [func accessibilityElement(children: AccessibilityChildBehavior) -> some View](view/accessibilityelement(children:).md)
  Creates a new accessibility element, or modifies the [`AccessibilityChildBehavior`](accessibilitychildbehavior.md) of the existing accessibility element.
- [func accessibilityChildren<V>(children: () -> V) -> some View](view/accessibilitychildren(children:).md)
  Replaces the existing accessibility element’s children with one or more new synthetic accessibility elements.
- [func accessibilityRepresentation<V>(representation: () -> V) -> some View](view/accessibilityrepresentation(representation:).md)
  Replaces one or more accessibility elements for this view with new accessibility elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessibilitychildbehavior)*