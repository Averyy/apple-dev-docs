# init(_:systemImage:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a new tab that you can use in a tab view using a system image for the tab item’s image, and a localized string key label.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init(_ titleResource: LocalizedStringResource, systemImage: String, @ContentBuilder content: () -> Content) where Label == DefaultTabLabel
```

Available when `Value` is `Never`, `Content` conforms to `View`, and `Label` conforms to `View`.

**Other overloads**:

```swift
init(_ titleKey: LocalizedStringKey, systemImage: String, @ContentBuilder content: () -> Content) where Label == DefaultTabLabel
```

```swift
init<S>(_ title: S, systemImage: String, @ContentBuilder content: () -> Content) where Label == DefaultTabLabel, S : StringProtocol
```

## Parameters

- `titleResource`: The localized string resource label for the tab’s tab item.
- `systemImage`: The image for the tab’s tab item.
- `content`: The view content of the tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tab/init(_:systemimage:content:)-4n3rq)*