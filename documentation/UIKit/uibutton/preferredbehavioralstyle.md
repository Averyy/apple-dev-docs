# preferredBehavioralStyle

**Framework**: UIKit  
**Kind**: property

The preferred behavioral style.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var preferredBehavioralStyle: UIBehavioralStyle { get set }
```

#### Discussion

Use this property to specify the behavioral style for the button. If the value of the property is [`UIBehavioralStyle.automatic`](uibehavioralstyle/automatic.md), use the [`behavioralStyle`](uibutton/behavioralstyle.md) property to determine the actual style.

The default value for [`preferredBehavioralStyle`](uibutton/preferredbehavioralstyle.md) is [`UIBehavioralStyle.automatic`](uibehavioralstyle/automatic.md). To learn more about behavioral styles, see [`UIBehavioralStyle`](uibehavioralstyle.md).

## See Also

- [var behavioralStyle: UIBehavioralStyle](uibutton/behavioralstyle.md)
  The style that determines how the button behaves.
- [enum UIBehavioralStyle](uibehavioralstyle.md)
  Constants that indicate how a control behaves in apps built with Mac Catalyst.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/preferredbehavioralstyle)*