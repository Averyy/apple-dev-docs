# sideBySide

**Framework**: Group Activities  
**Kind**: property

An arrangement where the participants sit in a line with the content in front of them.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
static let sideBySide: SpatialTemplatePreference
```

#### Discussion

The participants are side by side and face your app’s shared content. This arrangement works best for windows and other vertically oriented content. For example, you might use it for a group of participants watching a movie. However, you can apply it to any for other content configurations.

For example:

```swift
        App

A     B     C     D
```

## See Also

- [static let none: SpatialTemplatePreference](spatialtemplatepreference/none.md)
  An arrangement where the system places spatial Personas based on your app’s content.
- [static let conversational: SpatialTemplatePreference](spatialtemplatepreference/conversational.md)
  An arrangement where the participants can see one another and the app’s content.
- [static func custom(any SpatialTemplate) -> SpatialTemplatePreference](spatialtemplatepreference/custom(_:).md)
  Creates a template preference with the given custom spatial template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/spatialtemplatepreference/sidebyside)*