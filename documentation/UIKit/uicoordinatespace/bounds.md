# bounds

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

The bounds rectangle describing the item’s location and size in its own coordinate system.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var bounds: CGRect { get }
```

#### Discussion

The rectangle in this property always matches the app’s interface orientation. For apps that support all interface orientations, the value in this property can change when the user rotates the device between portrait and landscape modes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicoordinatespace/bounds)*