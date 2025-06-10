# synonyms

**Framework**: App Intents  
**Kind**: property

A list of localized phrases that are synonyms of this particular type display representation

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
var synonyms: [LocalizedStringResource]
```

#### Discussion

Example:

```swift
struct PizzaEntity: AppEntity {
    static var typeDisplayRepresentation = TypeDisplayRepresentation(
        name: "Pizza",
        synonyms: ["Pie", "Za"]
    )
}

```

In this case, we are saying that PizzaEntity can be represented as “Pizza”, “Pie” or “Za”


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/typedisplayrepresentation/synonyms)*