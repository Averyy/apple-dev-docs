# AppEntityUIElementsContext.ElementsRequest

**Framework**: App Intents  
**Kind**: enum  
**Role**: Enumeration

A type that describes which UI elements the system is requesting.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
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
- [AppEntityUIElementsContext.ElementsRequest.selected](./elementsrequest/selected.md)
  Any elements that are currently selected should be provided.
- [AppEntityUIElementsContext.ElementsRequest.visible(rect:)](./elementsrequest/visible%28rect%29.md)
  Any visible elements that intersect the given rect should be provided.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appentityuielementscontext/elementsrequest)*