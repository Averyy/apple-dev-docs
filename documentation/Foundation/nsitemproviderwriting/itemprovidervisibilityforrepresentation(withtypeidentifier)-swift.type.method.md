# itemProviderVisibilityForRepresentation(withTypeIdentifier:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Asks the item provider for the default representation visibility specification for the given UTI.

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
optional static func itemProviderVisibilityForRepresentation(withTypeIdentifier typeIdentifier: String) -> NSItemProviderRepresentationVisibility
```

```objc
+ (NSItemProviderRepresentationVisibility) itemProviderVisibilityForRepresentationWithTypeIdentifier:(NSString *) typeIdentifier;
```

## Return Value

A representation visibility specification for the given UTI.

## Parameters

- `typeIdentifier`: A uniform type identifier (UTI).

## See Also

### Getting the representation visibility specification
- [func itemProviderVisibilityForRepresentation(withTypeIdentifier: String) -> NSItemProviderRepresentationVisibility](./itemprovidervisibilityforrepresentation%28withtypeidentifier%29-swift.method.md)
  Asks the item provider for the representation visibility specification for the given UTI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemproviderwriting/itemprovidervisibilityforrepresentation(withtypeidentifier:)-swift.type.method)*