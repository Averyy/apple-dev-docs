# revert(_:)

**Framework**: AppKit  
**Kind**: method

Causes the receiver to discard any unsaved changes to bound user default properties, restoring their previous values.

**Availability**:
- macOS ?+

## Declaration

```swift
@IBAction
@MainActor func revert(_ sender: Any?)
```

#### Discussion

The receiver invokes [`discardEditing`](https://developer.apple.com/documentation/objectivec/nsobject/1458076-discardediting) on any currently registered editors. The `sender` is typically the object that invoked this method.

If [`appliesImmediately`](nsuserdefaultscontroller/appliesimmediately.md) is [`true`](https://developer.apple.com/documentation/swift/true), this method only causes any bound editors with uncommitted changes to discard their edits.

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
- [func revertToInitialValues(Any?)](nsuserdefaultscontroller/reverttoinitialvalues(_:).md)
  Causes the receiver to discard all edits and replace the values of all the user default properties with any corresponding values in the [`initialValues`](nsuserdefaultscontroller/initialvalues.md) dictionary.
- [func save(Any?)](nsuserdefaultscontroller/save(_:).md)
  Saves the values of the receiver’s user default properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserdefaultscontroller/revert(_:))*