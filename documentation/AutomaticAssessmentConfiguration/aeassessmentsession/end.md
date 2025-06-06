# end()

**Framework**: Automatic Assessment Configuration  
**Kind**: method

Ends an assessment session.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 14.0+
- macOS 10.15.4+

## Declaration

```swift
func end()
```

#### Discussion

Before calling the [`end()`](aeassessmentsession/end().md) method, be sure to stop the assessment and hide any sensitive information. After calling the method, wait until the session’s delegate receives the [`assessmentSessionDidEnd(_:)`](aeassessmentsessiondelegate/assessmentsessiondidend(_:).md) method before you report the assessment as complete to the user.

## See Also

- [func begin()](aeassessmentsession/begin.md)
  Starts an assessment session.
- [var isActive: Bool](aeassessmentsession/isactive.md)
  A Boolean that indicates whether an assessment session is running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentsession/end())*