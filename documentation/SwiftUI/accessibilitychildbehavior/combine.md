# combine

**Framework**: SwiftUI  
**Kind**: property

Any child accessibility element’s properties are merged into the new accessibility element.

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
static let combine: AccessibilityChildBehavior
```

#### Discussion

Use this behavior when you want a view represented by a single accessibility element. The new accessibility element merges properties from all non-hidden children. Some properties may be transformed or ignored to achieve the ideal combined result. For example, not all of [`AccessibilityTraits`](accessibilitytraits.md) are merged and a [`default`](accessibilityactionkind/default.md) action may become a named action ([`init(named:)`](accessibilityactionkind/init(named:).md)).

```swift
struct UserCell: View {
    var user: User

    var body: some View {
        VStack {
            Image(user.image)
            Text(user.name)
            Button("Options", action: showOptions)
        }
        .accessibilityElement(children: .combine)
    }
}
```

A new accessibility element is created when:

- The view contains multiple or zero accessibility elements
- The view wraps a [`UIViewRepresentable`](uiviewrepresentable.md)/[`NSViewRepresentable`](nsviewrepresentable.md).

> **Note**: If an accessibility element is not created, the [`AccessibilityChildBehavior`](accessibilitychildbehavior.md) of the existing accessibility element is modified.

## See Also

- [static let contain: AccessibilityChildBehavior](accessibilitychildbehavior/contain.md)
  Any child accessibility elements become children of the new accessibility element.
- [static let ignore: AccessibilityChildBehavior](accessibilitychildbehavior/ignore.md)
  Any child accessibility elements become hidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessibilitychildbehavior/combine)*