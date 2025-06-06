# show(relativeTo:of:preferredEdge:)

**Framework**: AppKit  
**Kind**: method

Shows the picker interface and populates it with the relevant sharing services.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func show(relativeTo rect: NSRect, of view: NSView, preferredEdge: NSRectEdge)
```

#### Discussion

In macOS 13 and later, the picker displays the macOS share sheet in a popover. In earlier versions of macOS, the picker displays a menu with the available services. When someone chooses a service for sharing the items, the picker notifies its delegate and then shares the content.

The following example shows the basic code to display the picker in response to an action. Update the code to include the items you want to share and to position the picker interface in an appropriate part of your window.

```objc
- (IBAction)share:(id)sender
{
    NSArray * items = @[];
    NSSharingServicePicker * picker = [[NSSharingServicePicker alloc] initWithItems:items];
    picker.delegate = self;
    [picker showRelativeToRect:[sender bounds] ofView:sender preferredEdge:NSMinYEdge];
}
```

## Parameters

- `rect`: The rectangle the picker should be showed relative to. The coordinates are in the   coordinate system. Passing   causes the view bounds to be used.
- `view`: The view.
- `preferredEdge`: The preferred edge of the view to display the picker. See   for the possible values.

## See Also

- [func close()](nssharingservicepicker/close.md)
  Closes the picker interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservicepicker/show(relativeto:of:preferrededge:))*