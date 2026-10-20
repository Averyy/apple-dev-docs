# init(_:animation:sectionBy:)

**Framework**: SwiftData  
**Kind**: init  
**Role**: Initializer

Creates a sectioned query from a fetch descriptor, grouped into sections by a required String key path.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
@MainActor
@preconcurrency init(_ descriptor: FetchDescriptor<Element>, animation: Animation, sectionBy sectionKeyPath: KeyPath<Element, String>) where Result == SectionedResults<Element, String>
```

Available when `Element` conforms to `PersistentModel`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/query/init(_:animation:sectionby:)-1yoyc)*