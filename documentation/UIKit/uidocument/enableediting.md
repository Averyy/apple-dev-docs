# enableEditing()

**Framework**: UIKit  
**Kind**: method

Enables editing when it’s safe again to make changes to a document.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func enableEditing()
```

#### Discussion

Subclasses should override this method to allow the user to edit the document when it’s safe to do so. This method override should be paired with an override of [`disableEditing()`](uidocument/disableediting().md). The default implementation of this method does nothing.

## See Also

- [func disableEditing()](uidocument/disableediting.md)
  Disables editing when it’s unsafe to make changes to a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/enableediting())*