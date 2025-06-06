# identifier

**Framework**: AppKit  
**Kind**: property

An optional, unique identifier for the storyboard segue that you can specify using the Identity inspector in Interface Builder.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var identifier: NSStoryboardSegue.Identifier? { get }
```

#### Discussion

You use this property if you override the [`prepare(for:sender:)`](nssegueperforming/prepare(for:sender:).md) method of the [`NSSeguePerforming`](nssegueperforming.md) protocol.

## See Also

- [var sourceController: Any](nsstoryboardsegue/sourcecontroller.md)
  The starting/containing view controller or window controller for the storyboard segue.
- [var destinationController: Any](nsstoryboardsegue/destinationcontroller.md)
  The ending/contained view controller or window controller for the storyboard segue.
- [NSStoryboardSegue.Identifier](nsstoryboardsegue/identifier-swift.typealias.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstoryboardsegue/identifier-swift.property)*