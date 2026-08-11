# attributeSet

**Framework**: App Intents  
**Kind**: property  
**Required**: Yes

A custom attribute set that you include with your entity to improve search accuracy.

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

Use this property to include additional metadata in the index for your app entity. This property augments the set of declared properties in your entity that have an indexing key. The default implementation of this property provides an attribute set with the title, subtitle, and image values from the entity’s display representation.

## See Also

- [var defaultAttributeSet: CSSearchableItemAttributeSet](indexedentity/defaultattributeset.md)
  The default set of attributes to include with your app entity in the Spotlight index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/indexedentity/attributeset)*