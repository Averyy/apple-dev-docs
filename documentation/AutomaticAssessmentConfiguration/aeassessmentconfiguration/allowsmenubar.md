# allowsMenuBar

**Framework**: Automatic Assessment Configuration  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to allow the menu bar during an assessment.

**Availability**:
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
var allowsMenuBar: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL allowsMenuBar;
```

## Discussion

An assessment session hides the menu bar by default, but you can allow it by setting [`allowsMenuBar`](./allowsmenubar.md) to `true` in the [`AEAssessmentConfiguration`](../aeassessmentconfiguration.md) instance that you use to initialize a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowsmenubar)*