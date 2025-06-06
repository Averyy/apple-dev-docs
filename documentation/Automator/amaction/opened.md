# opened()

**Framework**: Automator  
**Kind**: method

Allows the action to initialize its user interface.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
func opened()
```

#### Discussion

The system invokes this method when the action is first added to a workflow.

You should perform all initializations of an action’s user interface in this method and not in `awakeFromNib`. Be sure to invoke the superclass implementation of this method as the final step of your implementation.

## See Also

- [func activated()](amaction/activated.md)
  Allows the action to synchronize its information with settings in another app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amaction/opened())*