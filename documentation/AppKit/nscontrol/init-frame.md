# init(frame:)

**Framework**: AppKit  
**Kind**: init

Initializes a control with the specified frame rectangle.

**Availability**:
- macOS ?+

## Declaration

```swift
init(frame frameRect: NSRect)
```

#### Return Value

An initialized control object, or `nil` if the object couldn’t be initialized.

#### Discussion

If a cell has been specified for controls of this type, this method also creates an instance of the cell. Because `NSControl` is an abstract class, invocations of this method should appear only in the designated initializers of subclasses; that is, there should always be a more specific designated initializer for the subclass, as this method is the designated initializer for `NSControl`.

## Parameters

- `frameRect`: The rectangle of the control, specified in points in the coordinate space of the enclosing view.

## See Also

- [class NSControl](nscontrol.md)
  A specialized view, such as a button or text field, that notifies your app of relevant events using the target-action design pattern.
- [init?(coder: NSCoder)](nscontrol/init(coder:).md)
  Initializes a control with data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/init(frame:))*