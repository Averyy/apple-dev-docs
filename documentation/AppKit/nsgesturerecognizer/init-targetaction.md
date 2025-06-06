# init(target:action:)

**Framework**: AppKit  
**Kind**: init

Initializes the gesture recognizer with the specified target and action information.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
init(target: Any?, action: Selector?)
```

#### Return Value

The initialized gesture recognizer object or `nil` if an error occurred.

#### Discussion

This method is the designated initializer. Subclasses must call this method from their own custom initialization methods. Call the method before performing other tasks.

This method records the specified `target` and `action` values and prepares the gesture recognizer for use.

The `action` method must have one of the following signatures:

## Parameters

- `target`: The object whose action method is called when the gesture is recognized. You must not specify   for this parameter.
- `action`: A selector that identifies the method to call when the gesture is recognized. This method must be implemented by the object in  . You must not specify   for this parameter.

## See Also

- [var target: AnyObject?](nsgesturerecognizer/target.md)
  The object that implements the action method.
- [Cocoa Event Handling Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/EventOverview/Introduction/Introduction.html#//apple_ref/doc/uid/10000060i)
- [var action: Selector?](nsgesturerecognizer/action.md)
  The action method to call when the gesture is recognized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/init(target:action:))*