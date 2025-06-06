# init(identifier:source:destination:performHandler:)

**Framework**: AppKit  
**Kind**: init

Creates a storyboard segue and a block used when the segue is performed.

**Availability**:
- macOS 10.10+

## Declaration

```swift
convenience init(identifier: NSStoryboardSegue.Identifier, source sourceController: Any, destination destinationController: Any, performHandler: @escaping () -> Void)
```

#### Return Value

An initialized storyboard segue and code block, ready to be performed.

#### Discussion

You can use this method to customize a storyboard segue in lieu of creating a subclass.

## Parameters

- `identifier`: The unique identifier for the storyboard segue. See the   property.
- `sourceController`: The starting/containing view controller or window controller for the storyboard segue.
- `destinationController`: The ending/contained view controller or window controller for the storyboard segue.
- `performHandler`: A block of code that you provide, to be run each time the system calls the   method.

## See Also

- [init(identifier: NSStoryboardSegue.Identifier, source: Any, destination: Any)](nsstoryboardsegue/init(identifier:source:destination:).md)
  The designated initializer for a storyboard segue.
- [func perform()](nsstoryboardsegue/perform.md)
  Performs a visual transition from one controller to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstoryboardsegue/init(identifier:source:destination:performhandler:))*