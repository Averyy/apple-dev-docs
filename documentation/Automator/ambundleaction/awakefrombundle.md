# awakeFromBundle()

**Framework**: Automator  
**Kind**: method

Allows the action object to perform setup tasks requiring the presence of all bundle objects.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
func awakeFromBundle()
```

#### Discussion

The system sends this message to the action object when all objects in its bundle have been unarchived. Use this method to perform setup tasks such as adding the action object as an observer of notifications, dynamically establishing bindings, and dynamically setting targets and actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/ambundleaction/awakefrombundle())*