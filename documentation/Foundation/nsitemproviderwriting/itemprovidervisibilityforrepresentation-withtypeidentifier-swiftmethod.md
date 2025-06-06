# itemProviderVisibilityForRepresentation(withTypeIdentifier:)

**Framework**: Foundation  
**Kind**: method

Asks the item provider for the representation visibility specification for the given UTI.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
optional func itemProviderVisibilityForRepresentation(withTypeIdentifier typeIdentifier: String) -> NSItemProviderRepresentationVisibility
```

#### Return Value

A representation visibility specification for the given UTI.

## Parameters

- `typeIdentifier`: A uniform type identifier (UTI).

## See Also

- [static func itemProviderVisibilityForRepresentation(withTypeIdentifier: String) -> NSItemProviderRepresentationVisibility](nsitemproviderwriting/itemprovidervisibilityforrepresentation(withtypeidentifier:)-swift.type.method.md)
  Asks the item provider for the default representation visibility specification for the given UTI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemproviderwriting/itemprovidervisibilityforrepresentation(withtypeidentifier:)-swift.method)*