# delegate

**Framework**: Automator  
**Kind**: property  
**Role**: Instance Property

The controller’s delegate.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
weak var delegate: (any AMWorkflowControllerDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<AMWorkflowControllerDelegate> delegate;
```

#### Return Value

The controller’s delegate.

#### Discussion

This object receives updates on the progress and state of the workflow controller.

## See Also

### Accessing the Delegate
- [protocol AMWorkflowControllerDelegate](../amworkflowcontrollerdelegate.md)
  A set of optional methods that a delegate of a workflow controller implements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkflowcontroller/delegate)*