# NSUserDefaultsController

**Framework**: AppKit  
**Kind**: class

A controller that accesses user preference information for your app from the user’s defaults database.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSUserDefaultsController
```

#### Overview

[`NSUserDefaultsController`](nsuserdefaultscontroller.md) is a Cocoa bindings–compatible controller class. Properties of the shared instance of this class can be bound to user interface elements to access and modify values stored in [`UserDefaults`](https://developer.apple.com/documentation/Foundation/UserDefaults).

## Topics

### Obtaining the shared instance
- [class var shared: NSUserDefaultsController](nsuserdefaultscontroller/shared.md)
  Returns the shared instance of NSUserDefaultsController, creating it if necessary.
### Initializing a user defaults controller
- [init(defaults: UserDefaults?, initialValues: [String : Any]?)](nsuserdefaultscontroller/init(defaults:initialvalues:).md)
  Returns an initialized NSUserDefaultsController object using the NSUserDefaults instance specified in `defaults` and the initial default values contained in the `initialValues` dictionary.
- [init?(coder: NSCoder)](nsuserdefaultscontroller/init(coder:).md)
### Managing user defaults values
- [var defaults: UserDefaults](nsuserdefaultscontroller/defaults.md)
  Returns the instance of NSUserDefaults in use by the receiver.
- [var initialValues: [String : Any]?](nsuserdefaultscontroller/initialvalues.md)
  Returns a dictionary containing the receiver’s initial default values.
- [var hasUnappliedChanges: Bool](nsuserdefaultscontroller/hasunappliedchanges.md)
  Returns whether the receiver has user default values that have not been saved to NSUserDefaults.
- [var appliesImmediately: Bool](nsuserdefaultscontroller/appliesimmediately.md)
  Returns whether any changes made to bound user default properties are saved immediately.
- [var values: Any](nsuserdefaultscontroller/values.md)
  Returns a key value coding compliant object that is used to access the user default properties.
- [func revert(Any?)](nsuserdefaultscontroller/revert(_:).md)
  Causes the receiver to discard any unsaved changes to bound user default properties, restoring their previous values.
- [func revertToInitialValues(Any?)](nsuserdefaultscontroller/reverttoinitialvalues(_:).md)
  Causes the receiver to discard all edits and replace the values of all the user default properties with any corresponding values in the [`initialValues`](nsuserdefaultscontroller/initialvalues.md) dictionary.
- [func save(Any?)](nsuserdefaultscontroller/save(_:).md)
  Saves the values of the receiver’s user default properties.

## Relationships

### Inherits From
- [NSController](nscontroller.md)
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

- [class NSUbiquitousKeyValueStore](../Foundation/NSUbiquitousKeyValueStore.md)
  An iCloud-based container of key-value pairs you use to share data among instances of your app running on a user’s connected devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserdefaultscontroller)*