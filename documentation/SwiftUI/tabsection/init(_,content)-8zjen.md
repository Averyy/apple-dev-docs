# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a section with the provided content.

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
init(_ titleKey: LocalizedStringKey, @TabContentBuilder<SelectionValue> content: () -> Content) where Header == Text, Footer == EmptyView
```

Available when `Content` conforms to `TabContent` and `SelectionValue` conforms to `Hashable`.

**Other overloads**:

```swift
@export(implementation)
init(_ titleResource: LocalizedStringResource, @TabContentBuilder<SelectionValue> content: () -> Content) where Header == Text, Footer == EmptyView
```

```swift
@export(implementation)
init<V>(_ titleResource: LocalizedStringResource, @TabContentBuilder<V?> content: () -> Content) where Header == Text, Footer == EmptyView, SelectionValue == V?, V : Hashable
```

```swift
init<S>(_ title: S, @TabContentBuilder<SelectionValue> content: () -> Content) where Header == Text, Footer == EmptyView, S : StringProtocol
```

```swift
init<V, S>(_ title: S, @TabContentBuilder<V?> content: () -> Content) where Header == Text, Footer == EmptyView, SelectionValue == V?, V : Hashable, S : StringProtocol
```

```swift
init<V>(_ titleKey: LocalizedStringKey, @TabContentBuilder<V?> content: () -> Content) where Header == Text, Footer == EmptyView, SelectionValue == V?, V : Hashable
```

## Parameters

- `titleKey`: The localized string key label for the section’s header.
- `content`: The section’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabsection/init(_:content:)-8zjen)*