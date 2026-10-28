# invalidateTypeDescription(for:)

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Invalidates the type description for the given project type.

**Availability**:
- macOS 10.14+

## Declaration

```swift
func invalidateTypeDescription(for projectType: PHProjectType)
```

```objc
- (void) invalidateTypeDescriptionForProjectType:(PHProjectType) projectType;
```

## Discussion

If you call this method for project types other than [`undefined`](../phprojecttype/undefined.md), you must implement [`typeDescription(for:)`](../phprojecttypedescriptiondatasource/typedescription%28for%29.md) with functionality for the invalidated project type.

## Parameters

- `projectType`: The project type to invalidate.

## See Also

### Invalidating a Project Type
- [func invalidateFooterText(forSubtypesOf: PHProjectType)](./invalidatefootertext%28forsubtypesof%29.md)
  Invalidates the footer text for the subtypes of the given project type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojecttypedescriptioninvalidator/invalidatetypedescription(for:))*