# disableEditing()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Disables editing when it’s unsafe to make changes to a document.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func disableEditing()
```

```objc
- (void) disableEditing;
```

#### Discussion

Subclasses should override this method to prevent the user from editing the document when it’s unsafe to do so, such as during a save-and-close or revert operation. When editing is safe again, UIKit class calls [`enableEditing()`](./enableediting%28%29.md). The default implementation of this method does nothing.

## See Also

### Disabling and enabling editing
- [func enableEditing()](./enableediting%28%29.md)
  Enables editing when it’s safe again to make changes to a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/disableediting())*