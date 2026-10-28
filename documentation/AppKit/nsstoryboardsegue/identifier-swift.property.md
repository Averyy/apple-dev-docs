# identifier

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An optional, unique identifier for the storyboard segue that you can specify using the Identity inspector in Interface Builder.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var identifier: NSStoryboardSegue.Identifier? { get }
```

```objc
@property (copy, readonly, nullable) NSStoryboardSegueIdentifier identifier;
```

## Discussion

You use this property if you override the [`prepare(for:sender:)`](../nssegueperforming/prepare%28for,sender%29.md) method of the [`NSSeguePerforming`](../nssegueperforming.md) protocol.

## See Also

### Inspecting a Storyboard Segue
- [var sourceController: Any](./sourcecontroller.md)
  The starting/containing view controller or window controller for the storyboard segue.
- [var destinationController: Any](./destinationcontroller.md)
  The ending/contained view controller or window controller for the storyboard segue.
- [NSStoryboardSegue.Identifier](./identifier-swift.typealias.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstoryboardsegue/identifier-swift.property)*