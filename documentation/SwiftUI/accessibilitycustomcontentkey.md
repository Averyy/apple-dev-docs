# AccessibilityCustomContentKey

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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

## Overview

Use `AccessibilityCustomContentKey` and the associated modifiers taking this value as a parameter in order to simplify clearing or replacing entries of additional information that are manipulated from multiple places in your code.

## Topics

### Creating a key
- [init(_:)](./accessibilitycustomcontentkey/init%28_%29.md)
  Create an `AccessibilityCustomContentKey` with the specified label.
- [init(_:id:)](./accessibilitycustomcontentkey/init%28_,id%29.md)
  Create an `AccessibilityCustomContentKey` with the specified label and identifier.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)

## See Also

### Adding custom descriptions
- [func accessibilityCustomContent(_:_:importance:)](./view/accessibilitycustomcontent%28_,_,importance%29.md)
  Add additional accessibility information to the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessibilitycustomcontentkey)*