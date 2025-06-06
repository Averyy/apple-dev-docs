# begin()

**Framework**: Automatic Assessment Configuration  
**Kind**: method

Starts an assessment session.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 14.0+
- macOS 10.15.4+

## Declaration

```swift
func begin()
```

#### Discussion

After calling the [`begin()`](aeassessmentsession/begin().md) method, wait until the session’s delegate receives the [`assessmentSessionDidBegin(_:)`](aeassessmentsessiondelegate/assessmentsessiondidbegin(_:).md) method before starting an assessment or showing sensitive information. When you’re ready to stop the assessment session, call the [`end()`](aeassessmentsession/end().md) method.

## See Also

- [func end()](aeassessmentsession/end.md)
  Ends an assessment session.
- [var isActive: Bool](aeassessmentsession/isactive.md)
  A Boolean that indicates whether an assessment session is running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentsession/begin())*