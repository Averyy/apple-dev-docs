# showsCloseButton

**Framework**: CarPlay  
**Kind**: property

A Boolean value indicating whether the close button is allowed to appear.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
var showsCloseButton: Bool { get set }
```

#### Discussion

Set the value of this property to @c NO to hide the close button.

> **Note**: If the @c actions array is empty, the close button will be displayed regardless of this property’s value to ensure the alert remains dismissible.

Defaults to @c YES.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationalert/showsclosebutton)*