# AppEntityUIElementsContext.ElementsRequest

**Framework**: App Intents  
**Kind**: enum

A type that describes which UI elements the system is requesting.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
enum ElementsRequest
```

## Topics

### Enumeration Cases
- [AppEntityUIElementsContext.ElementsRequest.selected](appentityuielementscontext/elementsrequest/selected.md)
  Any elements that are currently selected should be provided.
- [AppEntityUIElementsContext.ElementsRequest.visible(rect:)](appentityuielementscontext/elementsrequest/visible(rect:).md)
  Any visible elements that intersect the given rect should be provided.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appentityuielementscontext/elementsrequest)*