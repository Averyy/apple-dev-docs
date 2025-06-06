# indexAppEntities(_:priority:)

**Framework**: Core Spotlight  
**Kind**: method

Indexes the provided entities into the system.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
func indexAppEntities(_ appEntities: [some IndexedEntity], priority: Int = 0) async throws
```

## Parameters

- `appEntities`: A list of donated entities to add to the index of donated entities.
- `priority`: The importance of this item compared to the other donated items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindex/indexappentities(_:priority:))*