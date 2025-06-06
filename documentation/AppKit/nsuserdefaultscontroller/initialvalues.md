# initialValues

**Framework**: AppKit  
**Kind**: property

Returns a dictionary containing the receiver’s initial default values.

**Availability**:
- macOS ?+

## Declaration

```swift
var initialValues: [String : Any]? { get set }
```

#### Discussion

These values are used when is no value found for the bound property in [`defaults`](nsuserdefaultscontroller/defaults.md).

This property is observable using key-value observing.

## See Also

- [var defaults: UserDefaults](nsuserdefaultscontroller/defaults.md)
  Returns the instance of NSUserDefaults in use by the receiver.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserdefaultscontroller/initialvalues)*