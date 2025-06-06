# dragItemsProvider

**Framework**: UIKit  
**Kind**: property

A closure that provides drag items that represent the document.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var dragItemsProvider: ((any UIDragSession) -> [UIDragItem])? { get set }
```

#### Discussion

To support drag and drop, assign a closure that returns an array of drag items that represent the document contents. When you set this property, a person can drag and drop the document from the navigation item’s title menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentproperties/dragitemsprovider)*