# subtypes(for:)

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Provides the root-level project type descriptions and descriptions of any promised subtypes with [`canProvideSubtypes`](../phprojecttypedescription/canprovidesubtypes.md) set to `true`.

**Availability**:
- macOS 10.14+

## Declaration

```swift
func subtypes(for projectType: PHProjectType) -> [PHProjectTypeDescription]
```

```objc
- (NSArray<PHProjectTypeDescription *> *) subtypesForProjectType:(PHProjectType) projectType;
```

## Return Value

An array of subtype descriptions for the queried project type.

## Parameters

- `projectType`: The project type whose subtypes are being requested. The value is [`undefined`](../phprojecttype/undefined.md) when fetching the root level.

## See Also

### Providing Required Fields
- [func typeDescription(for: PHProjectType) -> PHProjectTypeDescription?](./typedescription%28for%29.md)
  Provides the updated project type description for previously invalidated project types.
- [func footerText(forSubtypesOf: PHProjectType) -> NSAttributedString?](./footertext%28forsubtypesof%29.md)
  Provides the footer text for the subtypes of the given project type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojecttypedescriptiondatasource/subtypes(for:))*