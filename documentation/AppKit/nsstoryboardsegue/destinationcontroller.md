# destinationController

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The ending/contained view controller or window controller for the storyboard segue.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var destinationController: Any { get }
```

```objc
@property (strong, readonly) id destinationController;
```

#### Discussion

In your storyboard segue subclass, you can read this property to get the ending/contained view controller or window controller for the segue. This property is essential if you override the [`prepare(for:sender:)`](../nssegueperforming/prepare%28for,sender%29.md) method of the [`NSSeguePerforming`](../nssegueperforming.md) protocol, to let you pass configuration data to the ending/contained controller.

## See Also

### Inspecting a Storyboard Segue
- [var sourceController: Any](./sourcecontroller.md)
  The starting/containing view controller or window controller for the storyboard segue.
- [var identifier: NSStoryboardSegue.Identifier?](./identifier-swift.property.md)
  An optional, unique identifier for the storyboard segue that you can specify using the Identity inspector in Interface Builder.
- [NSStoryboardSegue.Identifier](./identifier-swift.typealias.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstoryboardsegue/destinationcontroller)*