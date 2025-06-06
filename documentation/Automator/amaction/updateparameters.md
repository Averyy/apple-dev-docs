# updateParameters()

**Framework**: Automator  
**Kind**: method

Requests the action to update its stored set of parameters from the settings in the action’s user interface.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
func updateParameters()
```

#### Discussion

This message sends just before an action is saved, copied, or run. Preferably, an action’s settings should not solely reside in the controls of its view, but if they do, the action can fetch and save them in this method.

## See Also

- [func parametersUpdated()](amaction/parametersupdated.md)
  Requests the action to update its user interface from its stored parameters, which have changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amaction/updateparameters())*