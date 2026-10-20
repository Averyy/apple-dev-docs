# Deprecated initializers

**Framework**: SwiftUI  
**Role**: API Collection

Review deprecated text field initializers.

#### Overview

Use view modifiers to specify change and commit behaviors for a text field when replacing these initializers. Use the [`onSubmit(of:_:)`](./view/onsubmit%28of,_%29.md) view modifier to get the behavior provided by the `onCommit` parameter. Use [`focused(_:equals:)`](./view/focused%28_,equals%29.md) and [`FocusState`](./focusstate.md) to get the behavior provided by the `onEditingChanged` parameter.

## Topics

### Creating a text field with a string
- [init(_:text:onEditingChanged:onCommit:)](./textfield/init%28_,text,oneditingchanged,oncommit%29.md)
  Creates a text field with a text label generated from a localized title string.
- [init(_:text:onCommit:)](./textfield/init%28_,text,oncommit%29.md)
  Creates a text field with a text label generated from a localized title string.
- [init(_:text:onEditingChanged:)](./textfield/init%28_,text,oneditingchanged%29.md)
  Creates a text field with a text label generated from a localized title string.
### Creating a text field with a value
- [init(_:value:formatter:onEditingChanged:onCommit:)](./textfield/init%28_,value,formatter,oneditingchanged,oncommit%29.md)
  Create an instance which binds over an arbitrary type, `V`.
- [init(_:value:formatter:onCommit:)](./textfield/init%28_,value,formatter,oncommit%29.md)
  Create an instance which binds over an arbitrary type, `V`.
- [init(_:value:formatter:onEditingChanged:)](./textfield/init%28_,value,formatter,oneditingchanged%29.md)
  Create an instance which binds over an arbitrary type, `V`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textfield-deprecated)*