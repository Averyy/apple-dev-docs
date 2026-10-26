# typeDescription(for:)

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Provides the updated project type description for previously invalidated project types.

**Availability**:
- macOS 10.14+

## Declaration

```swift
func typeDescription(for projectType: PHProjectType) -> PHProjectTypeDescription?
```

```objc
- (PHProjectTypeDescription *) typeDescriptionForProjectType:(PHProjectType) projectType;
```

#### Return Value

The [`PHProjectTypeDescription`](../phprojecttypedescription.md) for the given project type.  The returned description’s project type must match the given project type.

## Parameters

- `projectType`: The previously invalidated project type whose type description is being requested.

## See Also

### Providing Required Fields
- [func subtypes(for: PHProjectType) -> [PHProjectTypeDescription]](./subtypes%28for%29.md)
  Provides the root-level project type descriptions and descriptions of any promised subtypes with [`canProvideSubtypes`](../phprojecttypedescription/canprovidesubtypes.md) set to `true`.
- [func footerText(forSubtypesOf: PHProjectType) -> NSAttributedString?](./footertext%28forsubtypesof%29.md)
  Provides the footer text for the subtypes of the given project type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojecttypedescriptiondatasource/typedescription(for:))*