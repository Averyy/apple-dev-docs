# conversational

**Framework**: Group Activities  
**Kind**: property

An arrangement where the participants can see one another and the app’s content.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
static let conversational: SpatialTemplatePreference
```

#### Discussion

This arrangement works best when you want participants to converse with each other and also look at your app’s content.

For example:

```swift
      App

A             C

       B
```

## See Also

- [static let none: SpatialTemplatePreference](spatialtemplatepreference/none.md)
  An arrangement where the system places spatial Personas based on your app’s content.
- [static let sideBySide: SpatialTemplatePreference](spatialtemplatepreference/sidebyside.md)
  An arrangement where the participants sit in a line with the content in front of them.
- [static func custom(any SpatialTemplate) -> SpatialTemplatePreference](spatialtemplatepreference/custom(_:).md)
  Creates a template preference with the given custom spatial template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/spatialtemplatepreference/conversational)*