# revert(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Causes the receiver to discard any unsaved changes to bound user default properties, restoring their previous values.

**Availability**:
- macOS

## Declaration

```swift
@IBAction
func revert(_ sender: Any?)
```

```objc
- (void) revert:(id) sender;
```

## Discussion

The receiver invokes [`discardEditing`](../../ObjectiveC/nsobject-swift.class/discardediting.md) on any currently registered editors. The `sender` is typically the object that invoked this method.

If [`appliesImmediately`](./appliesimmediately.md) is [`true`](../../Swift/true.md), this method only causes any bound editors with uncommitted changes to discard their edits.

## See Also

### Managing user defaults values
- [var defaults: UserDefaults](./defaults.md)
  Returns the instance of NSUserDefaults in use by the receiver.
- [var initialValues: [String : Any]?](./initialvalues.md)
  Returns a dictionary containing the receiver’s initial default values.
- [var hasUnappliedChanges: Bool](./hasunappliedchanges.md)
  Returns whether the receiver has user default values that have not been saved to NSUserDefaults.
- [var appliesImmediately: Bool](./appliesimmediately.md)
  Returns whether any changes made to bound user default properties are saved immediately.
- [var values: Any](./values.md)
  Returns a key value coding compliant object that is used to access the user default properties.
- [func revertToInitialValues(Any?)](./reverttoinitialvalues%28_%29.md)
  Causes the receiver to discard all edits and replace the values of all the user default properties with any corresponding values in the [`initialValues`](./initialvalues.md) dictionary.
- [func save(Any?)](./save%28_%29.md)
  Saves the values of the receiver’s user default properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserdefaultscontroller/revert(_:))*