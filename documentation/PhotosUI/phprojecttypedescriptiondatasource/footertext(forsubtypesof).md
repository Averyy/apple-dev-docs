# footerText(forSubtypesOf:)

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Provides the footer text for the subtypes of the given project type.

**Availability**:
- macOS 10.14+

## Declaration

```swift
func footerText(forSubtypesOf projectType: PHProjectType) -> NSAttributedString?
```

```objc
- (NSAttributedString *) footerTextForSubtypesOfProjectType:(PHProjectType) projectType;
```

#### Return Value

Attributed footer text for the queried project type.

## Parameters

- `projectType`: The project type whose footer text is being requested. The value is [`undefined`](../phprojecttype/undefined.md) when fetching footer text at the root level.

## See Also

### Providing Required Fields
- [func subtypes(for: PHProjectType) -> [PHProjectTypeDescription]](./subtypes%28for%29.md)
  Provides the root-level project type descriptions and descriptions of any promised subtypes with [`canProvideSubtypes`](../phprojecttypedescription/canprovidesubtypes.md) set to `true`.
- [func typeDescription(for: PHProjectType) -> PHProjectTypeDescription?](./typedescription%28for%29.md)
  Provides the updated project type description for previously invalidated project types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojecttypedescriptiondatasource/footertext(forsubtypesof:))*