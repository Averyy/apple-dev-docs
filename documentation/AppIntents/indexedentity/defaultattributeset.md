# defaultAttributeSet

**Framework**: App Intents  
**Kind**: property

The default Spotlight attributes to associate with an entity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var defaultAttributeSet: CSSearchableItemAttributeSet { get }
```

#### Discussion

Use this property to get the default attributes for any entity. This attribute set contains the title value taken from the entity’s [`displayRepresentation`](instancedisplayrepresentable/displayrepresentation.md) property. If the display representation also provides values for the subtitle and image, this attribute set contains those values too.

If you create a custom attribute set for the [`attributeSet`](indexedentity/attributeset.md) property, add these default attributes in the new set you create.

## See Also

- [var attributeSet: CSSearchableItemAttributeSet](indexedentity/attributeset.md)
  The custom Spotlight attributes to associate with the entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/indexedentity/defaultattributeset)*