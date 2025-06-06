# markupText

**Framework**: UIKit  
**Kind**: property

The HTML markup text for the print formatter.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var markupText: String? { get set }
```

#### Discussion

When drawing begins for the print job, you cannot change the value of this property. The delegate method [`printInteractionControllerWillStartJob(_:)`](uiprintinteractioncontrollerdelegate/printinteractioncontrollerwillstartjob(_:).md) is called immediately before the formatting is set for the job.

## See Also

- [init(markupText: String)](uimarkuptextprintformatter/init(markuptext:).md)
  Returns a markup-text print formatter initialized with an HTML string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimarkuptextprintformatter/markuptext)*