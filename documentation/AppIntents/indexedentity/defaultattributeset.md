# defaultAttributeSet

**Framework**: App Intents  
**Kind**: property

The default set of attributes to include with your app entity in the Spotlight index.

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

This property contains an attribute set with the title, subtitle, and image values from the entity’s display representaiton. Provide any custom attributes for your entity using the [`attributeSet`](indexedentity/attributeset.md) property instead of this one.

## See Also

- [var attributeSet: CSSearchableItemAttributeSet](indexedentity/attributeset.md)
  A custom attribute set that you include with your entity to improve search accuracy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/indexedentity/defaultattributeset)*