# NSIsControllerMarker(_:)

**Framework**: AppKit  
**Kind**: func

Tests whether a given object is special marker object used for indicating the state of a selection in relation to a key.

**Availability**:
- macOS ?+

## Declaration

```swift
func NSIsControllerMarker(_ object: Any?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the object is one of the designated controller markers or [`false`](https://developer.apple.com/documentation/swift/false) if it is not.

#### Discussion

This function helps you to create bindings between user interface elements and controller objects. The Application Kit predefines several special marker objects used as values for indicating selection state; currently these are [`NSMultipleValuesMarker`](nsmultiplevaluesmarker.md), [`NSNoSelectionMarker`](nsnoselectionmarker.md), and [`NSNotApplicableMarker`](nsnotapplicablemarker.md). These markers are typed as `id` and only exist for the purpose of indicating a state; they are never archived and cannot be used as object values in controls. You use this function to test whether a given object value is a marker, in which case it is not directly assignable to the object that is bound. This check is important, especially since additional markers may be added in the future.

See the `NSKeyValueBinding.h` header file for further details.

## Parameters

- `object`: Specify the object you want to check. This parameter can be  .

## See Also

- [class NSDictionaryController](nsdictionarycontroller.md)
  A bindings-compatible controller that manages the display and editing of a dictionary of key-value pairs.
- [class NSDictionaryControllerKeyValuePair](nsdictionarycontrollerkeyvaluepair.md)
  A set of methods implemented by arranged objects to give access to information about those objects.
- [struct NSBindingName](nsbindingname.md)
  Values that specify a binding for certain methods.
- [struct NSBindingOption](nsbindingoption.md)
- [struct NSBindingInfoKey](nsbindinginfokey.md)
- [NSKeyValueBindingCreation](../ObjectiveC/nskeyvaluebindingcreation.md)
  A set of methods that you can use to create and remove bindings between view objects and controllers, or between controllers and model objects.
- [Binding dictionary keys](binding-dictionary-keys.md)
  These constants define keys in the binding information dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsiscontrollermarker(_:))*