# Binding dictionary keys

**Framework**: AppKit

These constants define keys in the binding information dictionary.

## Topics

### Constants
- [static let observedObject: NSBindingInfoKey](nsbindinginfokey/observedobject.md)
  The object that is the observable controller of the binding.
- [static let observedKeyPath: NSBindingInfoKey](nsbindinginfokey/observedkeypath.md)
  An `NSString` object containing the key path of the binding.
- [static let options: NSBindingInfoKey](nsbindinginfokey/options.md)
  An `NSDictionary` object containing key value pairs as specified in the options dictionary when the binding was created.

## See Also

- [class NSDictionaryController](nsdictionarycontroller.md)
  A bindings-compatible controller that manages the display and editing of a dictionary of key-value pairs.
- [class NSDictionaryControllerKeyValuePair](nsdictionarycontrollerkeyvaluepair.md)
  A set of methods implemented by arranged objects to give access to information about those objects.
- [struct NSBindingName](nsbindingname.md)
  Values that specify a binding for certain methods.
- [struct NSBindingOption](nsbindingoption.md)
- [struct NSBindingInfoKey](nsbindinginfokey.md)
- [func NSIsControllerMarker(Any?) -> Bool](nsiscontrollermarker(_:).md)
  Tests whether a given object is special marker object used for indicating the state of a selection in relation to a key.
- [NSKeyValueBindingCreation](../ObjectiveC/nskeyvaluebindingcreation.md)
  A set of methods that you can use to create and remove bindings between view objects and controllers, or between controllers and model objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/binding-dictionary-keys)*