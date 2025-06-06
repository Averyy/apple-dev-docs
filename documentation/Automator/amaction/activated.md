# activated()

**Framework**: Automator  
**Kind**: method

Allows the action to synchronize its information with settings in another app.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
func activated()
```

#### Discussion

The system invokes this method when the window of the Automator workflow to which the action belongs becomes the main window.

Be sure to invoke the superclass implementation of this method as the last thing in your implementation.

## See Also

- [func opened()](amaction/opened.md)
  Allows the action to initialize its user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amaction/activated())*