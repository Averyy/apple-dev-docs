# opened()

**Framework**: Automator  
**Kind**: method  
**Role**: Instance Method

Allows the action to initialize its user interface.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
func opened()
```

```objc
- (void) opened;
```

#### Discussion

The system invokes this method when the action is first added to a workflow.

You should perform all initializations of an action’s user interface in this method and not in `awakeFromNib`. Be sure to invoke the superclass implementation of this method as the final step of your implementation.

## See Also

### Initializing and Synchronizing the Action User Interface
- [func activated()](./activated%28%29.md)
  Allows the action to synchronize its information with settings in another app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amaction/opened())*