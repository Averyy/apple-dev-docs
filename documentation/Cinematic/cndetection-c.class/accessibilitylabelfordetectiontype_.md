# accessibilityLabelForDetectionType:

**Framework**: Cinematic  
**Kind**: method  
**Role**: Type Method

A localized accessibility label converting a specific detection type into a broad category such as a person, pet, and so on.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
+ (NSString *) accessibilityLabelForDetectionType:(CNDetectionType) detectionType;
```

## Return Value

A string representing a localized accessibility label converting a specific detection type into a broad category such as a person, pet, and so on.

## Parameters

- `detectionType`: The type of object to detect, such as the face, torso, cat, dog, and so on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cndetection-c.class/accessibilitylabelfordetectiontype:)*