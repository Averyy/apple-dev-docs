# markupText

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The HTML markup text for the print formatter.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var markupText: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * markupText;
```

#### Discussion

When drawing begins for the print job, you cannot change the value of this property. The delegate method [`printInteractionControllerWillStartJob(_:)`](../uiprintinteractioncontrollerdelegate/printinteractioncontrollerwillstartjob%28_%29.md) is called immediately before the formatting is set for the job.

## See Also

### Related Documentation
- [init(markupText: String)](./init%28markuptext%29.md)
  Returns a markup-text print formatter initialized with an HTML string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimarkuptextprintformatter/markuptext)*