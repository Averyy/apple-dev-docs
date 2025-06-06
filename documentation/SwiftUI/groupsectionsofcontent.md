# GroupSectionsOfContent

**Framework**: SwiftUI  
**Kind**: struct

Transforms the sections of a given view into a resulting content view.

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
struct GroupSectionsOfContent<Sections, Content> where Sections : View, Content : View
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
- [struct GroupElementsOfContent](groupelementsofcontent.md)
  Transforms the subviews of a given view into a resulting content view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/groupsectionsofcontent)*