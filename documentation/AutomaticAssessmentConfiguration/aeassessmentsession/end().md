# end()

**Framework**: Automatic Assessment Configuration  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) end;
```

## Discussion

Before calling the [`end()`](./end%28%29.md) method, be sure to stop the assessment and hide any sensitive information. After calling the method, wait until the session’s delegate receives the [`assessmentSessionDidEnd(_:)`](../aeassessmentsessiondelegate/assessmentsessiondidend%28_%29.md) method before you report the assessment as complete to the user.

## See Also

### Starting and stopping a session
- [func begin()](./begin%28%29.md)
  Starts an assessment session.
- [var isActive: Bool](./isactive.md)
  A Boolean that indicates whether an assessment session is running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentsession/end())*