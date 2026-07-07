# AppEntityUIElementsContext

**Framework**: App Intents  
**Kind**: struct

Contextual information for UI elements you make discoverable by Apple Intelligence.

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
struct AppEntityUIElementsContext
```

#### Overview

When you implement your custom app entity provider to make a custom view’s content discoverable by Apple Intelligence and Siri, you provide the system with [`AppEntityUIElement`](appentityuielement.md) objects that combine the app entity for a view’s content with additional information. The `AppEntityUIElementsContext` holds this additional information that the system uses to understand where content appears onscreen.

## Topics

### Instance Properties
- [let bounds: CGRect](appentityuielementscontext/bounds.md)
  The bounds that the system uses to understand the location of a UI element within the local coordinate space.
- [let requests: Set<AppEntityUIElementsContext.ElementsRequest>](appentityuielementscontext/requests.md)
  The set of requests for elements from the system.
### Enumerations
- [AppEntityUIElementsContext.ElementsRequest](appentityuielementscontext/elementsrequest.md)
  A type that describes which UI elements the system is requesting.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct AppEntityUIElement](appentityuielement.md)
  A type that wraps your app entity and adds information to make a custom view’s content discoverable by Apple Intelligence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appentityuielementscontext)*