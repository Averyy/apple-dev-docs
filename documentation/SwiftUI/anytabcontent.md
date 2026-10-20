# AnyTabContent

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

Type erased tab content.

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
nonisolated
struct AnyTabContent<SelectionValue> where SelectionValue : Hashable
```

## Topics

### Initializers
- [init<T>(T)](./anytabcontent/init%28_%29.md)
  Create an instance that type-erases `tabContent`.

## Relationships

### Conforms To
- [TabContent](./tabcontent.md)

## See Also

### Configuring a tab
- [func sectionActions<Content>(content: () -> Content) -> some View](./view/sectionactions%28content%29.md)
  Adds custom actions to a section.
- [struct TabPlacement](./tabplacement.md)
  A place that a tab can appear.
- [struct TabContentBuilder](./tabcontentbuilder.md)
  A result builder that constructs tabs for a tab view that supports programmatic selection. This builder requires that all tabs in the tab view have the same selection type.
- [protocol TabContent](./tabcontent.md)
  A type that provides content for programmatically selectable tabs in a tab view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/anytabcontent)*