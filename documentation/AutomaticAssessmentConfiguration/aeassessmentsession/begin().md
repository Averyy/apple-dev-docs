# begin()

**Framework**: Automatic Assessment Configuration  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) begin;
```

#### Discussion

After calling the [`begin()`](./begin%28%29.md) method, wait until the session’s delegate receives the [`assessmentSessionDidBegin(_:)`](../aeassessmentsessiondelegate/assessmentsessiondidbegin%28_%29.md) method before starting an assessment or showing sensitive information. When you’re ready to stop the assessment session, call the [`end()`](./end%28%29.md) method.

## See Also

### Starting and stopping a session
- [func end()](./end%28%29.md)
  Ends an assessment session.
- [var isActive: Bool](./isactive.md)
  A Boolean that indicates whether an assessment session is running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentsession/begin())*