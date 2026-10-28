# enableEditing()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Enables editing when it’s safe again to make changes to a document.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func enableEditing()
```

```objc
- (void) enableEditing;
```

## Discussion

Subclasses should override this method to allow the user to edit the document when it’s safe to do so. This method override should be paired with an override of [`disableEditing()`](./disableediting%28%29.md). The default implementation of this method does nothing.

## See Also

### Disabling and enabling editing
- [func disableEditing()](./disableediting%28%29.md)
  Disables editing when it’s unsafe to make changes to a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/enableediting())*