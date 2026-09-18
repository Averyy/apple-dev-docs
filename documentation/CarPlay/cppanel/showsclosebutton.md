# showsCloseButton

**Framework**: CarPlay  
**Kind**: property

A Boolean value that indicates whether the panel displays a close button.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
var showsCloseButton: Bool { get set }
```

#### Discussion

When the value of this property is `true`, the panel displays a close button that the driver can use to dismiss the panel. When the value of this property is `false`, you need to dismiss the panel programmatically from your app. The default value of this property is `true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cppanel/showsclosebutton)*