# init(context:)

**Framework**: Local Authentication Embedded UI  
**Kind**: init  
**Role**: Initializer

Creates a new authentication icon that reflects the current authentication state.

**Availability**:
- macOS 12.0+

## Declaration

```swift
init(context: LAContext)
```

```objc
- (instancetype) initWithContext:(LAContext *) context;
```

## Discussion

Use this initializer to create a local authentication view and connect it to a particular local authentication context. You typically do this in the [`loadView()`](../../AppKit/nsviewcontroller/loadview%28%29.md) method of an [`NSViewController`](../../AppKit/nsviewcontroller.md) subclass. You then add this view as a subview — along with any text, imagery, and interactive elements that you need — to create a custom authentication interface. When your interface appears, call the [`LAContext`](../../LocalAuthentication/lacontext.md) instance’s [`evaluatePolicy(_:localizedReason:reply:)`](../../LocalAuthentication/lacontext/evaluatepolicy%28_,localizedreason,reply%29.md) method to begin the authentication process.

## Parameters

- `context`: A local authentication context to associate with the icon.

## See Also

### Creating a local authentication view
- [var context: LAContext](./context.md)
  The local authentication context associated with the authentication view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthenticationembeddedui/laauthenticationview/init(context:))*