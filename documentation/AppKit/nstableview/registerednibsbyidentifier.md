# registeredNibsByIdentifier

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The dictionary of all registered nib files for view-based table view identifiers.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var registeredNibsByIdentifier: [NSUserInterfaceItemIdentifier : NSNib]? { get }
```

```objc
@property (copy, readonly, nullable) NSDictionary<NSString *,NSNib *> * registeredNibsByIdentifier;
```

## Discussion

Each key in the dictionary is the identifier string (given by [`NSUserInterfaceItemIdentifier`](../nsuserinterfaceitemidentifier.md)) used to register the nib file in the [`register(_:forIdentifier:)`](./register%28_,foridentifier%29.md) method. The value of each key is the corresponding [`NSNib`](../nsnib.md) object.

> **Note**:  This method applies only to [`NSView`](../nsview.md)-based table views.

## See Also

### NSView-Based Table Nib File Registration
- [func register(NSNib?, forIdentifier: NSUserInterfaceItemIdentifier)](./register%28_,foridentifier%29.md)
  Registers a NIB for the specified identifier, so that view-based table views can use it to instantiate views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/registerednibsbyidentifier)*