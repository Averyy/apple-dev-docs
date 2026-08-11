# init(_:)

**Framework**: App Intents  
**Kind**: init

Creates a URL representation for an app enum using the provided dictionary.

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
init(_ urlRepresentations: [Enum : EnumURLRepresentation<Enum>.EnumSingleURLRepresentation])
```

#### Discussion

Use this initializer when the URLs for each case differ significantly.

## Parameters

- `urlRepresentations`: A dictionary of enum values and strings. Use this dictionary to map different strings to each case of the enumeration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/enumurlrepresentation/init(_:)-1odm)*