# Animation

**Framework**: AppKit

Animate your views and other content to create a more engaging experience for users.

## Topics

### View-Based Animations
- [class NSViewAnimation](nsviewanimation.md)
  An animation of an app’s views, limited to changes in frame location and size, and to fade-in and fade-out effects.
- [protocol NSAnimatablePropertyContainer](nsanimatablepropertycontainer.md)
  A set of methods that defines a way to add animation to an existing class with a minimum of API impact.
- [class NSAnimationContext](nsanimationcontext.md)
  An animation context, which contains information about environment and state.
- [NSAnimation.Progress](nsanimation/progress.md)
  The animation progress, as a floating-point number between `0.0` and `1.0`.
- [enum NSAnimationEffect](nsanimationeffect.md)
  The type for standard system animation effects, which include both display and sound.
### Presentations
- [protocol NSViewControllerPresentationAnimator](nsviewcontrollerpresentationanimator.md)
  A set of methods that let you define animations to play when transitioning between two view controllers.
### Custom Animations
- [class NSAnimation](nsanimation.md)
  An object that manages the timing and progress of animations in the user interface.
- [protocol NSAnimationDelegate](nsanimationdelegate.md)
  A set of optional methods implemented by delegates of [`NSAnimation`](nsanimation.md) objects.

## See Also

- [Views and Controls](views-and-controls.md)
  Present your content onscreen and handle user input and events.
- [View Management](view-management.md)
  Manage your user interface, including the size and position of views in a window.
- [View Layout](view-layout.md)
  Position and size views using a stack view or Auto Layout constraints.
- [Appearance Customization](appearance-customization.md)
  Add Dark Mode support to your app, and use appearance proxies to modify your UI.
- [Windows, Panels, and Screens](windows-panels-and-screens.md)
  Organize your view hierarchies and facilitate their display onscreen.
- [Sound, Speech, and Haptics](sound-speech-and-haptics.md)
  Play sounds and haptic feedback, and incorporate speech recognition and synthesis into your interface.
- [Supporting Continuity Camera in Your Mac App](supporting-continuity-camera-in-your-mac-app.md)
  Incorporate scanned documents and pictures from a user’s iPhone, iPad, or iPod touch into your Mac app using Continuity Camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/animation)*