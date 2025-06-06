# GroupElementsOfContent

**Framework**: SwiftUI  
**Kind**: struct

Transforms the subviews of a given view into a resulting content view.

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
struct GroupElementsOfContent<Subviews, Content> where Subviews : View, Content : View
```

#### Overview

You don’t use this type directly. Instead SwiftUI creates this type on your behalf.

## Relationships

### Conforms To
- [View](view.md)

## See Also

- [Creating custom container views](creating-custom-container-views.md)
  Access individual subviews to compose flexible container views.
- [struct Group](group.md)
  A type that collects multiple instances of a content type — like views, scenes, or commands — into a single unit.
- [struct GroupSectionsOfContent](groupsectionsofcontent.md)
  Transforms the sections of a given view into a resulting content view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/groupelementsofcontent)*