# Visibility.hidden

**Framework**: SwiftUI  
**Kind**: case

The element may be hidden.

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
case hidden
```

#### Discussion

Some APIs may use this value to represent a hint or preference, rather than a mandatory assertion. For example, setting confirmation dialog title visibility to `hidden` using the [`confirmationDialog(_:isPresented:titleVisibility:actions:)`](view/confirmationdialog(_:ispresented:titlevisibility:actions:).md) modifier may not always hide the dialog title, which is required on some platforms.

## See Also

- [Visibility.automatic](visibility/automatic.md)
  The element may be visible or hidden depending on the policies of the component accepting the visibility configuration.
- [Visibility.visible](visibility/visible.md)
  The element may be visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/visibility/hidden)*