# Integrating pointer interactions into your iPad app

**Framework**: UIKit

Support touch interactions in your iPad app by adding pointer interactions to your views.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Xcode 12.5+

#### Overview

This sample code project shows how to use the [`UIPointerInteraction`](uipointerinteraction.md) class. A pointer interaction enables support for adding effects to a view, and for customizing the pointer’s appearance within a region of an app. It enhances user experience with mouse and trackpad devices and reduces the need for users to move their hands between a hardware keyboard and the touchscreen of an iPad. The sample places four shape views in a canvas within the app’s `ViewController`, each of which can be moved around. The shape views are a rectangle, oval, rounded rectangle, and triangle. Each of these takes on a different pointer effect when the user tracks the cursor over them. In addition, the sample shows a custom [`UIControl`](uicontrol.md) subclass, to illustrate how controls can adopt pointer interaction.

##### Add a Pointer Interaction to a Button

The sample adds a pointer interaction to a [`UIButton`](uibutton.md). Custom pointer interactions require a [`UIButtonPointerStyleProvider`](uibuttonpointerstyleprovider.md) function. When applying a style provider function, UIKit hands a pointer effect and pointer shape within that function to an app; the app then returns a pointer style for that particular button. Developers can pick and choose between the proposed effect and shape that the system recommends, replace one or the other, or create an entirely custom style. The sample applies four different pointer effects to its buttons: automatic, highlight, lift, and hover. For the fifth button a custom pointer hover effect is applied, so its effect remains the same size while hovered, and uses a custom [`UIPointerShape`](uipointershape-swift.enum.md).

##### Provide a Custom View for a Pointer Interaction

The sample implements shape views, which are a subclass of [`UIView`](uiview.md) called `ShapeView`. They interact with touch events with both the device’s touchscreen and touch pad. To visually interact with a shape view a [`UIPointerInteraction`](uipointerinteraction.md) object is assigned to it. View controllers adopt [`UIPointerInteractionDelegate`](uipointerinteractiondelegate.md) to help describe how that pointer interaction operates.

##### Add a Pointer Interaction to a View

A pointer interaction is described by a pointer style or visual representation. The pointer style is made up of both a [`UIPointerEffect`](uipointereffect-swift.enum.md) with a [`UITargetedPreview`](uitargetedpreview.md), and a [`UIPointerShape`](uipointershape-swift.enum.md). A commonly used shape for pointer effects is a rounded rectangle. A pointer shape or `UIPointerShape` requires a [`UIBezierPath`](uibezierpath.md), which describes that shape. The sample associates a pointer interaction to a shape view by adding one like this:

```swift
shapeView.addInteraction(UIPointerInteraction(delegate: self))
```

##### Create a Targeted Preview for a Pointer Interaction

For a shape view to describe its appearance during a pointer interaction, it must provide a [`UITargetedPreview`](uitargetedpreview.md). `UITargetedPreview` gives UIKit a view to which to apply an effect during pointer interactions:

```swift
func targetedPreview() -> UITargetedPreview? {
    let parameters = UIPreviewParameters()
    
    // Use the entire view's shape for the preview.
    let visiblePath = viewPath
    parameters.visiblePath = visiblePath
    
    return UITargetedPreview(view: self, parameters: parameters)
}
```

As the user moves the points within a shape view, the pointer interaction displays this targeted preview. Note that targeted previews are also used with context menus through the use of [`UIContextMenuConfiguration`](uicontextmenuconfiguration.md). In the sample, shape views have context menus.

##### Create a Pointer Effect for a Pointer Interaction

A pointer interaction needs a visual effect to describe how it will render the shape view’s targeted preview. The oval shape view, for example, uses [`UIPointerLiftEffect`](uipointerlifteffect.md), which slightly lifts the targeted preview and slides it around as the pointer is moved within the oval shape. The other shape views have their own pointer effects. The rectangle view uses a [`UIPointerEffect`](uipointereffect-swift.enum.md), a rounded rectangle view uses a [`UIPointerHighlightEffect`](uipointerhighlighteffect.md), and a triangle view uses a [`UIPointerHoverEffect`](uipointerhovereffect.md), which allows for its [`UIPointerShape`](uipointershape-swift.enum.md) to be revealed as a triangle.

##### Create a Shape for a Pointer Interaction

The Sample creates either region or shape, defined for each of its shape views, so a pointer interaction detects where to interact. The sample also implements [`pointerInteraction(_:regionFor:defaultRegion:)`](uipointerinteractiondelegate/pointerinteraction(_:regionfor:defaultregion:).md) as the [`UIPointerInteractionDelegate`](uipointerinteractiondelegate.md). This delegate is called by UIKit as the pointer moves within the pointer interaction’s view. Returning a [`UIPointerRegion`](uipointerregion.md) in which to apply a pointer style or returning `nil` indicates that this interaction does not customize the pointer for the current location.

```swift
func pointerInteraction(_ interaction: UIPointerInteraction,
                        regionFor request: UIPointerRegionRequest,
                        defaultRegion: UIPointerRegion) -> UIPointerRegion? {
    var pointerRegion: UIPointerRegion? = nil
    
    if let view = interaction.view as? ShapeView {
        // Pointer has entered one of the shape views.
 
        // Check for modifiers keys pressed while inside the view path.
        if request.modifiers.contains(.command) && request.modifiers.contains(.alternate) {
            // Command + Option was both pressed, dim the view.
            view.alpha = 0.50
        } else {
            if view.alpha != 1.0 { view.alpha = 1.0 }
        }
        
        // The user interacted with the inner path region.
        pointerRegion =
            UIPointerRegion(rect: view.innerPath.bounds,
                            identifier: ShapeView.regionIdentifier)
    } else if let view = interaction.view as? AlphaControl {
        // Pointer has entered the alpha control.
        if view.bounds.contains(request.location) {
            pointerRegion =
                UIPointerRegion(rect: view.bounds,
                                identifier: AlphaControl.regionIdentifier)
        }
    }
  
    return pointerRegion
}
```

The oval shape view, for example, interacts with the pointer from within its oval shaped [`UIBezierPath`](uibezierpath.md).

##### Interact with Views Using Gesture Recognizers

To make the shape views more interactive and provide custom behaviors driven by a mouse or trackpad, the sample attaches four different gesture recognizers to each shape view, to work alongside their pointer interactions.

A [`UIPanGestureRecognizer`](uipangesturerecognizer.md) moves a shape view and the frame color changes to orange when the command key is pressed during the pan gesture.

A [`UIPinchGestureRecognizer`](uipinchgesturerecognizer.md) changes the shape’s size with two-finger pinch gesture.

A [`UITapGestureRecognizer`](uitapgesturerecognizer.md) brings the tapped shape view to the front.

A [`UIHoverGestureRecognizer`](uihovergesturerecognizer.md) changes the frame color of a shape view to blue when the cursor is positioned over it. If the user presses the command key while hovering, the frame color toggles to pink.

Below is an example of handling the [`UIHoverGestureRecognizer`](uihovergesturerecognizer.md) to a `ShapeView`:

```swift
func hoverShape(_ gestureRecognizer: UIHoverGestureRecognizer) {
    guard let shapeViewToUse = gestureRecognizer.view as? ShapeView else { return }

    switch gestureRecognizer.state {
    case .began, .changed:
        // User hovered within the view's path, change the view's border color.
        var pathViewColor = UIColor.systemTeal
        if gestureRecognizer.modifierFlags.contains(.command) {
            // If the command key is pressed while hovering change frame color to pink.
            pathViewColor = UIColor.systemPink
        }
        shapeViewToUse.viewPathColor = pathViewColor
        shapeViewToUse.setNeedsDisplay()

    case .ended, .cancelled:
        // User left the view, restore the border color.
        shapeViewToUse.restoreOuterFrameColor()

    default:
        break
    }
}
```

##### Create a Gesture Recognizer for Continuous Scrolling

The [`UIPanGestureRecognizer`](uipangesturerecognizer.md) recognizes continuous scrolling that originates from devices like the trackpad. The sample adds a pan gesture recognizer to a custom [`UIControl`](uicontrol.md) subclass `AlphaControl`, that recognizes two-finger scroll gesture to change the alpha value of a given color. With [`allowedScrollTypesMask`](uipangesturerecognizer/allowedscrolltypesmask.md) set to [`continuous`](uiscrolltypemask/continuous.md), apps recognize continuous scrolling. The control’s color swatch changes as the user performs a pan scroll gesture, or through a direct touch.

## See Also

- [class UIPointerInteraction](uipointerinteraction.md)
  An interaction that enables support for effects on a view or customizes the pointer’s appearance within a region of an app.
- [protocol UIPointerInteractionDelegate](uipointerinteractiondelegate.md)
  An interface for handling pointer movements within the interaction’s view.
- [Enhancing your iPad app with pointer interactions](enhancing-your-ipad-app-with-pointer-interactions.md)
  Provide a great user experience with pointing devices, by incorporating pointer content effects and shape customizations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/integrating-pointer-interactions-into-your-ipad-app)*