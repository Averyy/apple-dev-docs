# IMKStateSetting

**Framework**: InputMethodKit  
**Kind**: protocol  
**Role**: Protocol

The `IMKStateSetting` protocol defines methods for setting or accessing values that indicate the state of an input method.

**Availability**:
- macOS 10.5+

## Declaration

```swift
protocol IMKStateSetting
```

```objc
@protocol IMKStateSetting
```

## Topics

### Activating and Deactivating the Server
- [func activateServer(Any!)](./imkstatesetting/activateserver%28_%29.md)
  Activates the input method server.
- [func deactivateServer(Any!)](./imkstatesetting/deactivateserver%28_%29.md)
  Deactivates the input method server.
### Showing a Preferences Window
- [func showPreferences(Any!)](./imkstatesetting/showpreferences%28_%29.md)
  Displays a preferences window.
### Getting the Supported Events
- [func recognizedEvents(Any!) -> Int](./imkstatesetting/recognizedevents%28_%29.md)
  Returns an unsigned integer that contains a union of event masks
### Getting the Mode Dictionary
- [func modes(Any!) -> [AnyHashable : Any]!](./imkstatesetting/modes%28_%29.md)
  Returns the modes dictionary associated with the input method.
### Getting and Setting Values
- [func value(forTag: Int, client: Any!) -> Any!](./imkstatesetting/value%28fortag,client%29.md)
  Returns a value object whose key is the provided tag.
- [func setValue(Any!, forTag: Int, client: Any!)](./imkstatesetting/setvalue%28_,fortag,client%29.md)
  Set the value for the provided key.

## Relationships

### Conforming Types
- [IMKInputController](./imkinputcontroller.md)

## See Also

### Protocols
- [protocol IMKMouseHandling](./imkmousehandling.md)
  The `IMKMouseHandling` protocol defines methods that your input method can implement to handle mouse events.
- [IMKServerInput](./imkserverinput.md)
  `IMKServerInput` is an informal protocol that defines methods for receiving text events. This is intentionally not a formal protocol because there are three ways to receive events. An input method chooses one of the following approaches and implements the appropriate methods:


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkstatesetting)*