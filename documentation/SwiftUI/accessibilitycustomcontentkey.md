# AccessibilityCustomContentKey

**Framework**: SwiftUI  
**Kind**: struct

Key used to specify the identifier and label associated with an entry of additional accessibility information.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct AccessibilityCustomContentKey
```

#### Overview

Use `AccessibilityCustomContentKey` and the associated modifiers taking this value as a parameter in order to simplify clearing or replacing entries of additional information that are manipulated from multiple places in your code.

## Topics

### Creating a key
- [init(LocalizedStringKey)](accessibilitycustomcontentkey/init(_:).md)
  Create an `AccessibilityCustomContentKey` with the specified label.
- [init(_:id:)](accessibilitycustomcontentkey/init(_:id:).md)
  Create an `AccessibilityCustomContentKey` with the specified label and identifier.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [func accessibilityCustomContent(_:_:importance:)](view/accessibilitycustomcontent(_:_:importance:).md)
  Add additional accessibility information to the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessibilitycustomcontentkey)*