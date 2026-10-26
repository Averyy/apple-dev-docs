# NSShowAnimationEffect

**Framework**: AppKit  
**Kind**: func  
**Role**: Function

Runs a system animation effect.

**Availability**:
- macOS 10.3+ - Deprecated in 14.0

> **Deprecated**: Use [`disappearingItem`](./nscursor/disappearingitem.md) instead.

## Declaration

```c
extern void NSShowAnimationEffect(NSAnimationEffect animationEffect, NSPoint centerLocation, NSSize size, id animationDelegate, SEL didEndSelector, void *contextInfo);
```

#### Discussion

This function runs one of the standard system animation effects, which includes display and sound. For example, you can use this function to display the puff of smoke effect. For a complete list of animation effects, see [`NSAnimationEffect`](./nsanimationeffect.md).

## Parameters

- `animationEffect`: The type of animation you want to apply.
- `centerLocation`: The location at which to show the animated image, specified in screen coordinates. The animation is centered on the point you specify.
- `size`: The desired size of the animated image. Specify [`NSZeroSize`](../Foundation/nszerosize.md) to perform the animation at the default size.
- `animationDelegate`: The object to notify when the animation completes. Specify `nil` if you do not need to be notified when the animation completes.
- `didEndSelector`: The selector of `animationDelegate` to call when the animation completes. Specify `nil` if you do not need to be notified when the animation completes. If you specify a selector, the corresponding method should have the following signature:

  ```objc
      - (void)animationEffectDidEnd:(void *)contextInfo;
  ```
- `contextInfo`: A pointer to any optional information you want passed as a parameter to the selector in the `didEndSelector` parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsshowanimationeffect)*