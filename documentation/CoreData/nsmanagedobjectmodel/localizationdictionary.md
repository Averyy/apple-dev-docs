# localizationDictionary

**Framework**: Core Data  
**Kind**: property

The localization dictionary of the model.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var localizationDictionary: [String : String]? { get set }
```

#### Discussion

The following table describes the key and value pattern for the localization dictionary.

| Key | Value | Note |
| --- | --- | --- |
| “Entity/NonLocalizedEntityName” | “LocalizedEntityName” |  |
| “Property/NonLocalizedPropertyName/Entity/EntityName” | “LocalizedPropertyName” | (1) |
| “Property/NonLocalizedPropertyName” | “LocalizedPropertyName” |  |
| “ErrorString/NonLocalizedErrorString” | “LocalizedErrorString” |  |

(1) For properties in different entities with the same non-localized name but that should have different localized names.

##### Special Considerations

In OS X v10.4, `localizationDictionary` may return `nil` until Core Data lazily loads the dictionary for its own purposes (for example, reporting a localized error).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/localizationdictionary)*