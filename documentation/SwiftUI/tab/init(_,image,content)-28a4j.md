# init(_:image:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a new tab that you can use in a tab view, with a string label.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init<S>(_ title: S, image: String, @ContentBuilder content: () -> Content) where Label == DefaultTabLabel, S : StringProtocol
```

Available when `Value` is `Never`, `Content` conforms to `View`, and `Label` conforms to `View`.

**Other overloads**:

```swift
init(_ titleKey: LocalizedStringKey, image: String, @ContentBuilder content: () -> Content) where Label == DefaultTabLabel
```

```swift
init(_ titleResource: LocalizedStringResource, image: String, @ContentBuilder content: () -> Content) where Label == DefaultTabLabel
```

## Parameters

- `title`: The label for the tab’s tab item.
- `image`: The image for the tab’s tab item.
- `content`: The view content of the tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tab/init(_:image:content:)-28a4j)*