# EventKitUIBundle()

**Framework**: EventKit UI  
**Kind**: func

Use to access resources within the app bundle.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
func EventKitUIBundle() -> Bundle!
```

#### Discussion

A  is a directory with a standardized hierarchical structure that holds executable code and the resources used by that code. Bundles organize their contained resources into well-defined subdirectories.

By using a bundle object, you can access a bundle’s resources without knowing the structure of the bundle. The bundle object provides a single interface for locating items, taking into account the bundle structure, user preferences, available localizations, and other relevant factors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkitui/eventkituibundle())*