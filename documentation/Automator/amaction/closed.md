# closed()

**Framework**: Automator  
**Kind**: method

Invoked by Automator when the receiving action is removed from a workflow, allowing it to perform cleanup operations.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.5+

## Declaration

```swift
func closed()
```

#### Discussion

This method is intended to be overridden, so that your action can perform its specific cleanup operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amaction/closed())*