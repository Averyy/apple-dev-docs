# sourceController

**Framework**: AppKit  
**Kind**: property

The starting/containing view controller or window controller for the storyboard segue.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var sourceController: Any { get }
```

#### Discussion

In your storyboard segue subclass, you can read this property to get the starting/containing view controller or window controller for the segue.

## See Also

- [var destinationController: Any](nsstoryboardsegue/destinationcontroller.md)
  The ending/contained view controller or window controller for the storyboard segue.
- [var identifier: NSStoryboardSegue.Identifier?](nsstoryboardsegue/identifier-swift.property.md)
  An optional, unique identifier for the storyboard segue that you can specify using the Identity inspector in Interface Builder.
- [NSStoryboardSegue.Identifier](nsstoryboardsegue/identifier-swift.typealias.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstoryboardsegue/sourcecontroller)*