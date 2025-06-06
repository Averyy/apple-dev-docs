# init(_:value:)

**Framework**: SwiftUI  
**Kind**: init

Creates a navigation link that presents the view corresponding to a codable value, with a text label that the link generates from a localized string key.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
init<P>(_ titleKey: LocalizedStringKey, value: P?) where Label == Text, P : Decodable, P : Encodable, P : Hashable
```

## Mentions

- [Understanding the navigation stack](understanding-the-composition-of-navigation-stack.md)

#### Discussion

When someone activates the navigation link that this initializer creates, SwiftUI looks for a nearby [`navigationDestination(for:destination:)`](view/navigationdestination(for:destination:).md) view modifier with a `data` input parameter that matches the type of this initializer’s `value` input, with one of the following outcomes:

- If SwiftUI finds a matching modifier within the view hierarchy of an enclosing [`NavigationStack`](navigationstack.md), it pushes the modifier’s corresponding `destination` view onto the stack.
- If SwiftUI finds a matching modifier in the view hierarchy of a stack that’s in a later column of a [`NavigationSplitView`](navigationsplitview.md), it puts the modifier’s destination view as the first and only item onto the stack while preserving the stack’s root view.
- If there’s no matching modifier, but the link appears in a [`List`](list.md) with selection inside a leading column of a navigation split view, the link updates the selection, which might affect the appearance of a trailing view. For an example of this, see [`NavigationLink`](navigationlink.md).
- In other cases, the link doesn’t do anything.

Because this initializer takes a value that conforms to the [`Codable`](https://developer.apple.com/documentation/Swift/Codable) protocol, you ensure that a [`NavigationPath`](navigationpath.md) that includes this link can produce a non-`nil` value for its [`codable`](navigationpath/codable.md) property. This helps to make the path serializable.

## Parameters

- `titleKey`: A localized string that describes the view that this link   presents.
- `value`: An optional value to present. When someone   taps or clicks the link, SwiftUI stores a copy of the value.   Pass a   value to disable the link.

## See Also

- [init(value:label:)](navigationlink/init(value:label:).md)
  Creates a navigation link that presents the view corresponding to a codable value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationlink/init(_:value:))*