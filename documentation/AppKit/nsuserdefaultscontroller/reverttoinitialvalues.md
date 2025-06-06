# revertToInitialValues(_:)

**Framework**: AppKit  
**Kind**: method

Causes the receiver to discard all edits and replace the values of all the user default properties with any corresponding values in the [`initialValues`](nsuserdefaultscontroller/initialvalues.md) dictionary.

**Availability**:
- macOS ?+

## Declaration

```swift
@IBAction
@MainActor func revertToInitialValues(_ sender: Any?)
```

#### Discussion

This effectively sets the preferences that a user can change to their “out-of-the-box” values. This method has no effect if initial values were not specified. The `sender` is typically the object that invoked this method.

## See Also

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
- [func save(Any?)](nsuserdefaultscontroller/save(_:).md)
  Saves the values of the receiver’s user default properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserdefaultscontroller/reverttoinitialvalues(_:))*