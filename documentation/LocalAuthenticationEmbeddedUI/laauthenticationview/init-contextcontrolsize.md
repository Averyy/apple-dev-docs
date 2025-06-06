# init(context:controlSize:)

**Framework**: Local Authentication Embedded UI  
**Kind**: init

Creates a new authentication icon that reflects the current authentication state, using a specified size.

**Availability**:
- macOS 12.0+

## Declaration

```swift
@MainActor
init(context: LAContext, controlSize: NSControl.ControlSize)
```

#### Discussion

This initializer behaves like [`init(context:)`](laauthenticationview/init(context:).md), except that it also allows you to specify a size for the view. If you don’t specify a size, the view uses the [`NSControl.ControlSize.regular`](https://developer.apple.com/documentation/AppKit/NSControl/ControlSize-swift.enum/regular) size by default.

## Parameters

- `context`: A local authentication context to associate with the icon.
- `controlSize`: The size of the authentication view’s user interface element. Use one of the values   in  .

## See Also

- [var controlSize: NSControl.ControlSize](laauthenticationview/controlsize.md)
  The size of the local authentication view user interface element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthenticationembeddedui/laauthenticationview/init(context:controlsize:))*