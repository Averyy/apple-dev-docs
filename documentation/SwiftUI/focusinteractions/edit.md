# edit

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The view captures input from non-spatial sources like a keyboard or Digital Crown.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static let edit: FocusInteractions
```

#### Discussion

Views that support focus-driven editing interactions become focused when the user taps or clicks on them, or when the user issues a focus movement command.

## See Also

### Creating the interaction types
- [static var automatic: FocusInteractions](./automatic.md)
  The view supports whatever focus-driven interactions are commonly expected for interactive content on the current platform.
- [static let activate: FocusInteractions](./activate.md)
  The view has a primary action that can be activated via focus gestures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/focusinteractions/edit)*