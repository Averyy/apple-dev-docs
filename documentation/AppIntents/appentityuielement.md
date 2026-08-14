# AppEntityUIElement

**Framework**: App Intents  
**Kind**: struct

A type that wraps your app entity and adds information to make a custom view’s content discoverable by Apple Intelligence.

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
struct AppEntityUIElement
```

## Mentions

- [Providing contextual cues to Apple Intelligence and Siri](providing-contextual-cues-to-apple-intelligence-and-siri.md)

#### Overview

A custom view where your app manages state for the user interface or you use custom drawing to render the interface. For example, you might use a custom list or tab implementation and manage selection and other states in the app, or you might use Metal to render the interface. If either applies to your app’s interface, make content discoverable by Apple Intelligence using `appEntityUIElementProvider` and provide the system with a list of `AppEntityUIElements`.

When your app uses a custom view and your app manages its state or you use custom drawing to render a UI element, you need to implement your own `appEntityUIElementProvider`. This closure provides the system with `AppEntityUIElement` objects that combine the app entity for your content and additional information with spatial and state information to help the system understand onscreen content.

For more information, refer to doc:providing-contextual-cues-to-Apple-Intelligence-and-Siri and [`App Intents`](AppIntents.md).

## Topics

### Structures
- [AppEntityUIElement.State](appentityuielement/state-swift.struct.md)
  The current UI state of the entity that’s visible onscreen.
### Initializers
- [init<Entity>(Entity, bounds: CGRect, state: AppEntityUIElement.State, subelements: [AppEntityUIElement])](appentityuielement/init(_:bounds:state:subelements:).md)
  Creates a wrapper object that combines an app entity with additional information to make it discoverable by Apple Intelligence and Siri.
- [init(identifier: EntityIdentifier, bounds: CGRect, state: AppEntityUIElement.State, subelements: [AppEntityUIElement])](appentityuielement/init(identifier:bounds:state:subelements:).md)
  Creates a wrapper object that combines an app entity with additional information to make it discoverable by Apple Intelligence and Siri.
### Instance Properties
- [var bounds: CGRect](appentityuielement/bounds.md)
  The bounds of the content in the view’s local coordinate space.
- [var identifier: EntityIdentifier](appentityuielement/identifier.md)
  The identifier of the app entity that represents the UI element.
- [var state: AppEntityUIElement.State](appentityuielement/state-swift.property.md)
  The property that indicates if the UI element is selected.
- [var subelements: [AppEntityUIElement]](appentityuielement/subelements.md)
  An array of UI elements that represent subelements in the view hierarchy.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct AppEntityUIElementsContext](appentityuielementscontext.md)
  Contextual information for UI elements you make discoverable by Apple Intelligence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appentityuielement)*