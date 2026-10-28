# init(context:controlSize:)

**Framework**: Local Authentication Embedded UI  
**Kind**: init  
**Role**: Initializer

Creates a new authentication icon that reflects the current authentication state, using a specified size.

**Availability**:
- macOS 12.0+

## Declaration

```swift
init(context: LAContext, controlSize: NSControl.ControlSize)
```

```objc
- (instancetype) initWithContext:(LAContext *) context controlSize:(NSControlSize) controlSize;
```

## Discussion

This initializer behaves like [`init(context:)`](./init%28context%29.md), except that it also allows you to specify a size for the view. If you don’t specify a size, the view uses the [`NSControl.ControlSize.regular`](../../AppKit/nscontrol/controlsize-swift.enum/regular.md) size by default.

## Parameters

- `context`: A local authentication context to associate with the icon.
- `controlSize`: The size of the authentication view’s user interface element. Use one of the values in [`NSControl.ControlSize`](../../AppKit/nscontrol/controlsize-swift.enum.md).

## See Also

### Controlling the size of a local authentication view
- [var controlSize: NSControl.ControlSize](./controlsize.md)
  The size of the local authentication view user interface element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthenticationembeddedui/laauthenticationview/init(context:controlsize:))*