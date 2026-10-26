# invalidateFooterText(forSubtypesOf:)

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Invalidates the footer text for the subtypes of the given project type.

**Availability**:
- macOS 10.14+

## Declaration

```swift
func invalidateFooterText(forSubtypesOf projectType: PHProjectType)
```

```objc
- (void) invalidateFooterTextForSubtypesOfProjectType:(PHProjectType) projectType;
```

#### Discussion

Use [`undefined`](../phprojecttype/undefined.md) to invalidate the root-level footer text.

## Parameters

- `projectType`: The project type whose subtypes you’d like to invalidate.

## See Also

### Invalidating a Project Type
- [func invalidateTypeDescription(for: PHProjectType)](./invalidatetypedescription%28for%29.md)
  Invalidates the type description for the given project type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojecttypedescriptioninvalidator/invalidatefootertext(forsubtypesof:))*