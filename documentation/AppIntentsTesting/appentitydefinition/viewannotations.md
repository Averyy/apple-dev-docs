# viewAnnotations()

**Framework**: App Intents Testing  
**Kind**: method

Provides the currently visible onscreen entities.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func viewAnnotations() async throws -> [ViewAnnotation]
```

## Mentions

- [Testing your App Intents code](testing-your-app-intents-code.md)

#### Return Value

An array of view annotations, with selection state and entity data.

#### Discussion

> **Note**: An error if the view annotations query fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/appentitydefinition/viewannotations())*