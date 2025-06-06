# perform()

**Framework**: AppKit  
**Kind**: method

Performs a visual transition from one controller to another.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func perform()
```

#### Discussion

You can override this method in your [`NSStoryboardSegue`](nsstoryboardsegue.md) subclass to perform custom animation between the starting/containing controller and the ending/contained controller for a storyboard segue. Typically, you would use Core Animation to set up an animation from one set of views to the next. For more complex animations, you might take a snapshot image of the two view hierarchies and manipulate the images instead of the view objects.

Regardless of how you perform the animation, you are responsible for installing the destination view controller o window controller (and its contained views) in the right place so that it can handle events. Typically, this entails calling one of the presentation methods in the [`NSViewController`](nsviewcontroller.md) class.

## See Also

- [convenience init(identifier: NSStoryboardSegue.Identifier, source: Any, destination: Any, performHandler: () -> Void)](nsstoryboardsegue/init(identifier:source:destination:performhandler:).md)
  Creates a storyboard segue and a block used when the segue is performed.
- [init(identifier: NSStoryboardSegue.Identifier, source: Any, destination: Any)](nsstoryboardsegue/init(identifier:source:destination:).md)
  The designated initializer for a storyboard segue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstoryboardsegue/perform())*