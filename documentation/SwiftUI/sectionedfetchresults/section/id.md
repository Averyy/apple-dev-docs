# id

**Framework**: SwiftUI  
**Kind**: property

The value that all entities in the section share for a specified key path.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@MainActor
@preconcurrency let id: SectionIdentifier
```

#### Discussion

Specify the key path that the entities share this value with by setting the [`SectionedFetchRequest`](sectionedfetchrequest.md) instance’s `sectionIdentifier` parameter during initialization, or by modifying the corresponding [`SectionedFetchResults`](sectionedfetchresults.md) instance’s [`sectionIdentifier`](sectionedfetchresults/sectionidentifier.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sectionedfetchresults/section/id)*