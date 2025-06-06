# save(_:)

**Framework**: AppKit  
**Kind**: method

Saves the values of the receiver’s user default properties.

**Availability**:
- macOS ?+

## Declaration

```swift
@IBAction
@MainActor func save(_ sender: Any?)
```

#### Discussion

This method has no effect if [`appliesImmediately`](nsuserdefaultscontroller/appliesimmediately.md) returns [`true`](https://developer.apple.com/documentation/swift/true).

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
- [func revertToInitialValues(Any?)](nsuserdefaultscontroller/reverttoinitialvalues(_:).md)
  Causes the receiver to discard all edits and replace the values of all the user default properties with any corresponding values in the [`initialValues`](nsuserdefaultscontroller/initialvalues.md) dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserdefaultscontroller/save(_:))*