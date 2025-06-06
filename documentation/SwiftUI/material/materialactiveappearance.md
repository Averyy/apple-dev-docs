# materialActiveAppearance(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets an explicit active appearance for this material.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func materialActiveAppearance(_ appearance: MaterialActiveAppearance) -> Material
```

#### Discussion

Materials used as the `window` container background on macOS will automatically appear inactive when their the window appears inactive, but can be made to always appear active by setting the active appearance behavior to be always active:

```swift
Text("Hello, World!")
    .containerBackground(
        Material.regular.materialActiveAppearance(.active),
        for: .window)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/material/materialactiveappearance(_:))*