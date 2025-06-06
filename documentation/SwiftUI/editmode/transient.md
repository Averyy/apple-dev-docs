# EditMode.transient

**Framework**: SwiftUI  
**Kind**: case

The view is in a temporary edit mode.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
case transient
```

#### Discussion

The use of this state varies by platform and for different controls. As an example, SwiftUI might engage temporary edit mode over the duration of a swipe gesture.

The [`isEditing`](editmode/isediting.md) property is `true` in this state.

## See Also

- [EditMode.active](editmode/active.md)
  The user can edit the view content.
- [EditMode.inactive](editmode/inactive.md)
  The user can’t edit the view content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/editmode/transient)*