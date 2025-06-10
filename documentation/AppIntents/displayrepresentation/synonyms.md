# synonyms

**Framework**: App Intents  
**Kind**: property

A list of localized phrases that are synonyms of this particular display representation

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
DisplayRepresentation(
    name: "Pizza",
    synonyms: ["Pie", "Za"]
)
```

In this case, “Pie”, “Za” and “Pizza” are all ways to display this


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/displayrepresentation/synonyms)*