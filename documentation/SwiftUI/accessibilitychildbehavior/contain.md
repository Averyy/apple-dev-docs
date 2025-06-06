# contain

**Framework**: Swiftui  
**Kind**: property

Any child accessibility elements become children of the new accessibility element.

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
static let contain: AccessibilityChildBehavior
```

#### Discussion

Use this behavior when you want a view to be an accessibility container. An accessibility container groups child accessibility elements which improves navigation. For example, all children of an accessibility container are navigated in order before navigating through the next accessibility container.

```swift
var body: some View {
    ScrollView {
        VStack {
            HStack {
                ForEach(users) { user in
                    UserCell(user)
                }
            }
            .accessibilityElement(children: .contain)
            .accessibilityLabel("Users")

            VStack {
                ForEach(messages) { message in
                    MessageCell(message)
                }
            }
            .accessibilityElement(children: .contain)
            .accessibilityLabel("Messages")
        }
    }
}
```

A new accessibility element is created when:

- The view contains multiple or zero accessibility elements
- The view contains a single accessibility element with no children

> **Note**: If an accessibility element is not created, the [`AccessibilityChildBehavior`](accessibilitychildbehavior.md) of the existing accessibility element is modified.

## See Also

- [static let combine: AccessibilityChildBehavior](accessibilitychildbehavior/combine.md)
  Any child accessibility element’s properties are merged into the new accessibility element.
- [static let ignore: AccessibilityChildBehavior](accessibilitychildbehavior/ignore.md)
  Any child accessibility elements become hidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/SwiftUI/accessibilitychildbehavior/contain)*