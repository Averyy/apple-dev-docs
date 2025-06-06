# IMKStateSetting

**Framework**: InputMethodKit  
**Kind**: protocol

The `IMKStateSetting` protocol defines methods for setting or accessing values that indicate the state of an input method.

**Availability**:
- macOS 10.5+

## Declaration

```swift
protocol IMKStateSetting
```

## Topics

### Activating and Deactivating the Server
- [func activateServer(Any!)](imkstatesetting/activateserver(_:).md)
  Activates the input method server.
- [func deactivateServer(Any!)](imkstatesetting/deactivateserver(_:).md)
  Deactivates the input method server.
### Showing a Preferences Window
- [func showPreferences(Any!)](imkstatesetting/showpreferences(_:).md)
  Displays a preferences window.
### Getting the Supported Events
- [func recognizedEvents(Any!) -> Int](imkstatesetting/recognizedevents(_:).md)
  Returns an unsigned integer that contains a union of event masks
### Getting the Mode Dictionary
- [func modes(Any!) -> [AnyHashable : Any]!](imkstatesetting/modes(_:).md)
  Returns the modes dictionary associated with the input method.
### Getting and Setting Values
- [func value(forTag: Int, client: Any!) -> Any!](imkstatesetting/value(fortag:client:).md)
  Returns a value object whose key is the provided tag.
- [func setValue(Any!, forTag: Int, client: Any!)](imkstatesetting/setvalue(_:fortag:client:).md)
  Set the value for the provided key.

## Relationships

### Conforming Types
- [IMKInputController](imkinputcontroller.md)

## See Also

- [protocol IMKMouseHandling](imkmousehandling.md)
  The `IMKMouseHandling` protocol defines methods that your input method can implement to handle mouse events.
- [IMKServerInput](imkserverinput.md)
  `IMKServerInput` is an informal protocol that defines methods for receiving text events. This is intentionally not a formal protocol because there are three ways to receive events. An input method chooses one of the following approaches and implements the appropriate methods:


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkstatesetting)*