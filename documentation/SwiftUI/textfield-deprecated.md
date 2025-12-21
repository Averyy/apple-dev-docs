# Deprecated initializers

**Framework**: SwiftUI

Review deprecated text field initializers.

#### Overview

Use view modifiers to specify change and commit behaviors for a text field when replacing these initializers. Use the [`onSubmit(of:_:)`](view/onsubmit(of:_:).md) view modifier to get the behavior provided by the `onCommit` parameter. Use [`focused(_:equals:)`](view/focused(_:equals:).md) and [`FocusState`](focusstate.md) to get the behavior provided by the `onEditingChanged` parameter.

## Topics

### Creating a text field with a string
- [init(_:text:onEditingChanged:onCommit:)](textfield/init(_:text:oneditingchanged:oncommit:).md)
  Creates a text field with a text label generated from a localized title string.
- [init(_:text:onCommit:)](textfield/init(_:text:oncommit:).md)
  Creates a text field with a text label generated from a localized title string.
- [init(_:text:onEditingChanged:)](textfield/init(_:text:oneditingchanged:).md)
  Creates a text field with a text label generated from a localized title string.
### Creating a text field with a value
- [init(_:value:formatter:onEditingChanged:onCommit:)](textfield/init(_:value:formatter:oneditingchanged:oncommit:).md)
  Create an instance which binds over an arbitrary type, `V`.
- [init(_:value:formatter:onCommit:)](textfield/init(_:value:formatter:oncommit:).md)
  Create an instance which binds over an arbitrary type, `V`.
- [init(_:value:formatter:onEditingChanged:)](textfield/init(_:value:formatter:oneditingchanged:).md)
  Create an instance which binds over an arbitrary type, `V`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textfield-deprecated)*