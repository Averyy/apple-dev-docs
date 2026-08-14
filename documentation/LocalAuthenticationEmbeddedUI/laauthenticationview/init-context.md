# init(context:)

**Framework**: Local Authentication Embedded UI  
**Kind**: init

Creates a new authentication icon that reflects the current authentication state.

**Availability**:
- macOS 12.0+

## Declaration

```swift
init(context: LAContext)
```

#### Discussion

Use this initializer to create a local authentication view and connect it to a particular local authentication context. You typically do this in the [`loadView()`](https://developer.apple.com/documentation/appkit/nsviewcontroller/loadview()) method of an [`NSViewController`](https://developer.apple.com/documentation/appkit/nsviewcontroller) subclass. You then add this view as a subview — along with any text, imagery, and interactive elements that you need — to create a custom authentication interface. When your interface appears, call the [`LAContext`](https://developer.apple.com/documentation/localauthentication/lacontext) instance’s [`evaluatePolicy(_:localizedReason:reply:)`](https://developer.apple.com/documentation/localauthentication/lacontext/evaluatepolicy(_:localizedreason:reply:)) method to begin the authentication process.

## Parameters

- `context`: A local authentication context to associate with the icon.

## See Also

- [var context: LAContext](laauthenticationview/context.md)
  The local authentication context associated with the authentication view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthenticationembeddedui/laauthenticationview/init(context:))*