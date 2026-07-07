# attributeSet

**Framework**: App Intents  
**Kind**: property  
**Required**: Yes

The custom Spotlight attributes to associate with the entity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var attributeSet: CSSearchableItemAttributeSet { get }
```

## Mentions

- [Making app entities available in Spotlight](making-app-entities-available-in-spotlight.md)

#### Discussion

If you don’t provide a value for this property, the default implementation returns the contents of the [`defaultAttributeSet`](indexedentity/defaultattributeset.md) property. If you assign a new value to this property, the property returns your new set instead.

When you create a custom attribute set, add the contents of the [`defaultAttributeSet`](indexedentity/defaultattributeset.md) if you want to include them in your new set. The system doesn’t add the default attributes automatically.

During indexing, Spotlight indexes the values in this set together with any entity properties that have an associated indexing key. For information about how to specify entity-related attributes, see [`Making app entities available in Spotlight`](making-app-entities-available-in-spotlight.md).

## See Also

- [var defaultAttributeSet: CSSearchableItemAttributeSet](indexedentity/defaultattributeset.md)
  The default Spotlight attributes to associate with an entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/indexedentity/attributeset)*