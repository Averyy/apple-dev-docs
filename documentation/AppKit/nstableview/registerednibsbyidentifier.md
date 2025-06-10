# registeredNibsByIdentifier

**Framework**: AppKit  
**Kind**: property

The dictionary of all registered nib files for view-based table view identifiers.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
var registeredNibsByIdentifier: [NSUserInterfaceItemIdentifier : NSNib]? { get }
```

#### Discussion

Each key in the dictionary is the identifier string (given by [`NSUserInterfaceItemIdentifier`](nsuserinterfaceitemidentifier.md)) used to register the nib file in the [`register(_:forIdentifier:)`](nstableview/register(_:foridentifier:).md) method. The value of each key is the corresponding [`NSNib`](nsnib.md) object.

> **Note**:  This method applies only to [`NSView`](nsview.md)-based table views.

## See Also

- [func register(NSNib?, forIdentifier: NSUserInterfaceItemIdentifier)](nstableview/register(_:foridentifier:).md)
  Registers a NIB for the specified identifier, so that view-based table views can use it to instantiate views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/registerednibsbyidentifier)*