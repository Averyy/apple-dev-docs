# NSDictionaryController

**Framework**: AppKit  
**Kind**: class

A bindings-compatible controller that manages the display and editing of a dictionary of key-value pairs.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class NSDictionaryController
```

#### Overview

[`NSDictionaryController`](nsdictionarycontroller.md) transforms the contents of a dictionary into an array of key-value pairs that can be bound to user interface items such as the columns of an [`NSTableView`](nstableview.md).

The content of an [`NSDictionaryController`](nsdictionarycontroller.md) instance is specified using the inherited method [`content`](nsobjectcontroller/content.md) or by binding an [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary) instance to the [`contentDictionary`](nsbindingname/contentdictionary.md) binding. New key/value pairs inserted into the dictionary are created using the [`newObject()`](nsdictionarycontroller/newobject().md) method. The initial key name is set to the string returned by [`initialKey`](nsdictionarycontroller/initialkey.md) . The initial key name is copied to the newly inserted object, while the object returned by [`initialValue`](nsdictionarycontroller/initialvalue.md) is simply retained. As new items are inserted the controller enumerates the initial key name, resulting in key names such as “key”, “key1”, “key2”, and so on. This behavior can be customized by overriding [`newObject()`](nsdictionarycontroller/newobject().md).

An [`NSDictionaryController`](nsdictionarycontroller.md) instance can be configured to exclude specified keys in a dictionary from being returned by [`arrangedObjects`](nsarraycontroller/arrangedobjects.md) using the [`excludedKeys`](nsdictionarycontroller/excludedkeys.md) property. Similarly, you can specify an array of key names that are always included in the arranged objects, even if they are not present in the content dictionary, using the [`includedKeys`](nsdictionarycontroller/includedkeys.md) property.

[`NSDictionaryController`](nsdictionarycontroller.md) supports providing localized key names for the keys in the dictionary, allowing a user-friendly representation of the key name to be displayed. The localized key names are specified by a dictionary (using [`localizedKeyDictionary`](nsdictionarycontroller/localizedkeydictionary.md)) or by providing a strings table (using [`localizedKeyDictionary`](nsdictionarycontroller/localizedkeydictionary.md)).

The [`arrangedObjects`](nsarraycontroller/arrangedobjects.md) method returns an array of objects that implement the [`NSDictionaryControllerKeyValuePair`](nsdictionarycontrollerkeyvaluepair.md) informal protocol. User interface controls are bound to the arranged objects array using key paths such as: `arrangedObjects.key` (displays the key name), `arrangedObjects.value` (displays the value for the key), or `arrangedObjects.localizedKey` (displays the localized key name). See [`NSDictionaryControllerKeyValuePair`](nsdictionarycontrollerkeyvaluepair.md) for more information.

> **Note**:  You must enable the “Validates Immediately” option for the value binding of all controls that edit the key names or values returned by [`arrangedObjects`](nsarraycontroller/arrangedobjects.md).

 You must enable the “Validates Immediately” option for the value binding of all controls that edit the key names or values returned by [`arrangedObjects`](nsarraycontroller/arrangedobjects.md).

[`NSDictionaryController`](nsdictionarycontroller.md) overrides [`arrangedObjects`](nsarraycontroller/arrangedobjects.md) to return an array of objects that implement the [`NSDictionaryControllerKeyValuePair`](nsdictionarycontrollerkeyvaluepair.md) informal protocol. See [`NSDictionaryControllerKeyValuePair`](nsdictionarycontrollerkeyvaluepair.md) and [`Cocoa Bindings Programming Topics`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaBindings/CocoaBindings.html#//apple_ref/doc/uid/10000167i) for more information.

The constants listed below are used to specify a binding to [`bind(_:to:withKeyPath:options:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/bind(_:to:withKeyPath:options:)), [`infoForBinding(_:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/infoForBinding(_:)), [`unbind(_:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/unbind(_:)), and [`valueClassForBinding(_:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/valueClassForBinding(_:)). See the [`Cocoa Bindings Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Reference/CocoaBindingsRef/CocoaBindingsRef.html#//apple_ref/doc/uid/10000189i) for more information.

- [`contentDictionary`](nsbindingname/contentdictionary.md)
- [`includedKeys`](nsbindingname/includedkeys.md)
- [`excludedKeys`](nsbindingname/excludedkeys.md)
- [`localizedKeyDictionary`](nsbindingname/localizedkeydictionary.md)
- [`initialKey`](nsbindingname/initialkey.md)
- [`initialValue`](nsbindingname/initialvalue.md)

## Topics

### Arranging Objects
- [var arrangedObjects: Any](nsarraycontroller/arrangedobjects.md)
  An array containing the receiver’s content objects arranged using [`arrange(_:)`](nsarraycontroller/arrange(_:).md).
### Creating New Entries
- [func newObject() -> NSDictionaryControllerKeyValuePair](nsdictionarycontroller/newobject.md)
  Creates and returns a new key-value pair to represent an entry in the content dictionary.
### Localizing Key Names
- [var localizedKeyDictionary: [String : String]](nsdictionarycontroller/localizedkeydictionary.md)
  The localized key names that are displayed by the receiver in place of the key names.
- [var localizedKeyTable: String?](nsdictionarycontroller/localizedkeytable.md)
  the strings file used to localize key names.
### Keys to Display
- [var includedKeys: [String]](nsdictionarycontroller/includedkeys.md)
  The key names that are represented by a key-value pair, even if they are not present in the receiver’s content dictionary.
- [var excludedKeys: [String]](nsdictionarycontroller/excludedkeys.md)
  The key names that are never displayed in the user interface items bound to the receiver.
### Setting Initial Key and Values
- [var initialKey: String](nsdictionarycontroller/initialkey.md)
  The string used as the initial key name for a newly inserted item.
- [var initialValue: Any](nsdictionarycontroller/initialvalue.md)
  The string used as the initial value for a newly inserted item.

## Relationships

### Inherits From
- [NSArrayController](nsarraycontroller.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSEditor](nseditor.md)
- [NSEditorRegistration](nseditorregistration.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

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
- [Binding dictionary keys](binding-dictionary-keys.md)
  These constants define keys in the binding information dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdictionarycontroller)*