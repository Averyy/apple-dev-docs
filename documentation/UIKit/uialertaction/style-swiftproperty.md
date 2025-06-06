# style

**Framework**: UIKit  
**Kind**: property

The style that applies to the action’s button.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var style: UIAlertAction.Style { get }
```

#### Discussion

This property is set to the value you specified in the [`init(title:style:handler:)`](uialertaction/init(title:style:handler:).md) method.

## See Also

- [var title: String?](uialertaction/title.md)
  The title of the action’s button.
- [var isEnabled: Bool](uialertaction/isenabled.md)
  A Boolean value indicating whether the action is currently enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertaction/style-swift.property)*