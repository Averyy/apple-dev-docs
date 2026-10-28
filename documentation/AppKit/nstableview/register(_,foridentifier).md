# register(_:forIdentifier:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Registers a NIB for the specified identifier, so that view-based table views can use it to instantiate views.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func register(_ nib: NSNib?, forIdentifier identifier: NSUserInterfaceItemIdentifier)
```

```objc
- (void) registerNib:(NSNib *) nib forIdentifier:(NSUserInterfaceItemIdentifier) identifier;
```

## Discussion

Use this method to associate one of the NIB’s cell views with `identifier` so that the table can instantiate this view when requested. This method is used when [`makeView(withIdentifier:owner:)`](./makeview%28withidentifier,owner%29.md) is called, and there was no NIB created at design time for the specified identifier. This allows dynamic loading of NIBs that can be associated with the table.

Because a NIB can contain multiple views, you can associate the same NIB with multiple identifiers. To remove a previously associated NIB for `identifier`, pass in `nil` for the `nib` value.

> **Note**:  This method applies only to [`NSView`](../nsview.md)-based table views.

## Parameters

- `nib`: The nib containing the view.
- `identifier`: The identifier of the view to create.

## See Also

### NSView-Based Table Nib File Registration
- [var registeredNibsByIdentifier: [NSUserInterfaceItemIdentifier : NSNib]?](./registerednibsbyidentifier.md)
  The dictionary of all registered nib files for view-based table view identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/register(_:foridentifier:))*