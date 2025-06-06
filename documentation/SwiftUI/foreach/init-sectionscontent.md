# init(sections:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates an instance that uniquely identifies and creates views across updates based on the sections of a given view.

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
init<V>(sections view: V, @ViewBuilder content: @escaping (SectionConfiguration) -> Content) where Data == ForEachSectionCollection<Content>, ID == SectionConfiguration.ID, Content : View, V : View
```

## Parameters

- `view`: The view to extract the sections of.
- `content`: The view builder that creates views from sections


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/foreach/init(sections:content:))*