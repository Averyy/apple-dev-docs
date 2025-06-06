# NSDictionaryControllerKeyValuePair

**Framework**: AppKit  
**Kind**: class

A set of methods implemented by arranged objects to give access to information about those objects.

**Availability**:
- macOS 10.11+

## Declaration

```swift
class NSDictionaryControllerKeyValuePair
```

#### Overview

[`NSDictionaryControllerKeyValuePair`](nsdictionarycontrollerkeyvaluepair.md) is an informal protocol that is implemented by objects returned by the [`NSDictionaryController`](nsdictionarycontroller.md) method arrangedObjects. See [`NSDictionaryController`](nsdictionarycontroller.md) for more information.

## Topics

### Instance Properties
- [var isExplicitlyIncluded: Bool](nsdictionarycontrollerkeyvaluepair/isexplicitlyincluded.md)
- [var key: String?](nsdictionarycontrollerkeyvaluepair/key.md)
- [var localizedKey: String?](nsdictionarycontrollerkeyvaluepair/localizedkey.md)
- [var value: Any?](nsdictionarycontrollerkeyvaluepair/value.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSDictionaryController](nsdictionarycontroller.md)
  A bindings-compatible controller that manages the display and editing of a dictionary of key-value pairs.
- [struct NSBindingName](nsbindingname.md)
  Values that specify a binding for certain methods.
- [struct NSBindingOption](nsbindingoption.md)
- [struct NSBindingInfoKey](nsbindinginfokey.md)
- [func NSIsControllerMarker(Any?) -> Bool](nsiscontrollermarker(_:).md)
  Tests whether a given object is special marker object used for indicating the state of a selection in relation to a key.
- [NSKeyValueBindingCreation](../ObjectiveC/nskeyvaluebindingcreation.md)
  A set of methods that you can use to create and remove bindings between view objects and controllers, or between controllers and model objects.
- [Binding dictionary keys](binding-dictionary-keys.md)
  These constants define keys in the binding information dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdictionarycontrollerkeyvaluepair)*