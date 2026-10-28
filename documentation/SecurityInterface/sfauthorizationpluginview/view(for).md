# view(for:)

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Returns the appropriate view object for the specified view type.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func view(for inType: SFViewType) -> NSView!
```

```objc
- (NSView *) viewForType:(SFViewType) inType;
```

## Return Value

An [`NSView`](../../AppKit/nsview.md) object representing either a credentials view or an identity and credentials view.

## Discussion

When the authorization plug-in calls this method, the [`SFAuthorizationPluginView`](../sfauthorizationpluginview.md) instance should return the [`NSView`](../../AppKit/nsview.md) object that represents the view indicated by the specified [`SFViewType`](../sfviewtype.md). The [`NSView`](../../AppKit/nsview.md) object and its contents should have the autoresize flags set to allow the view to be resized.

Note that although a maximum width of 394 points is currently supported, this may change in the future. You should not assume that the width of the [`NSView`](../../AppKit/nsview.md) object will never change.

## Parameters

- `inType`: The type of view being requested by the authorization plug-in.

## See Also

### Responding to User Actions
- [func buttonPressed(SFButtonType)](./buttonpressed%28_%29.md)
  Tells the authorization plug-in that the user pressed a button in the custom view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationpluginview/view(for:))*