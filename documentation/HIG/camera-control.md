---
url: https://developer.apple.com/design/human-interface-guidelines/camera-control
framework: HIG
---

# Camera Control

**Type:** article

**Platforms:** ios

> **Updated 2024-09-09:** New page.

The Camera Control provides direct access to your app’s camera experience.

![A stylized representation of the Camera Control.](https://docs-assets.developer.apple.com/published/9239b5856180c2fab15588576504e73b/inputs-camera-control-intro~dark%402x.png)
On iPhone 16 and iPhone 16 Pro models, the Camera Control quickly opens your app’s camera experience to capture moments as they happen. When a person lightly presses the Camera Control, the system displays an overlay that extends from the device bezel.
![A screenshot showing callouts to the Camera Control and overlay on iPhone in landscape orientation.](https://docs-assets.developer.apple.com/published/86935ae3e603d1483bce9fdf96111780/camera-control-button-callout~dark%402x.png)
The overlay allows people to quickly adjust controls. A person can view the available controls by lightly double-pressing the Camera Control. After selecting a control, they can slide their finger on the Camera Control to adjust a value to capture their content as they want.
![A partial screenshot of the Camera Control overlay displaying its controls.](https://docs-assets.developer.apple.com/published/31c4ed5e680391df09aeb669b744b4cf/camera-control-picker~dark%402x.png)

## Anatomy
The Camera Control offers two types of controls for adjusting values or changing between options:
- A *slider* provides a range of values to choose from, such as how much contrast to apply to the content.
- A *picker* offers discrete options, such as turning a grid on and off in the viewfinder.
![A partial screenshot of the Camera Control overlay displaying a slider control.](https://docs-assets.developer.apple.com/published/64c3152033a1ad80399fbae5361329bb/camera-control-slider-control~dark%402x.png)
![A partial screenshot of the Camera Control overlay displaying a picker control.](https://docs-assets.developer.apple.com/published/050de81138e4df1b0b0da22f6a04d8d8/camera-control-picker-control~dark%402x.png)
In addition to custom controls that you create, the system provides a set of standard controls that you can optionally include in the overlay to allow someone to adjust their camera’s zoom and exposure.
![A partial screenshot of the Camera Control overlay displaying the system zoom factor control.](https://docs-assets.developer.apple.com/published/64c3152033a1ad80399fbae5361329bb/system-control-type-zoom-factor~dark%402x.png)
![A partial screenshot of the Camera Control overlay displaying the system exposure bias control.](https://docs-assets.developer.apple.com/published/6ae4ee762416bd6dcdc9cf8ff2eddf8b/system-control-type-exposure-bias~dark%402x.png)

## Best practices
**Use SF Symbols to represent control functionality.** The system doesn’t support custom symbols; instead, pick a symbol from SF Symbols that clearly denotes a control’s behavior. iOS offers thousands of symbols you can use to represent the controls your app shows in the overlay. Symbols for controls don’t represent their current state. To view available symbols, see the Camera & Photos section in the [SF Symbols app](https://developer.apple.com/sf-symbols/).
![A partial screenshot of the Camera Control overlay displaying a camera flash control that uses the bolt.fill symbol.](https://docs-assets.developer.apple.com/published/0a8e7e5c6d612fce4b225949fb586fc3/camera-control-picker-sf-symbols-flash~dark%402x.png)
![A partial screenshot of the Camera Control overlay displaying a camera filters control that uses the camera.filters symbol.](https://docs-assets.developer.apple.com/published/63b5bc9d1a3abd240ceffb0f9852b96d/camera-control-picker-sf-symbols-filters~dark%402x.png)
**Keep names of controls short.** Control labels adhere to Dynamic Type sizes, and longer names may obfuscate the camera’s viewfinder.
**Include units or symbols with slider control values to provide context.** Providing descriptive information in the overlay, such as EV, %, or a custom string, helps people understand what the slider controls. For developer guidance, see [localizedValueFormat](../AVFoundation/AVCaptureSlider/localizedValueFormat.md).
![A partial screenshot showing an example of the Camera Control overlay with a slider control displaying a value and context for the type of value.](https://docs-assets.developer.apple.com/published/153d69c058cb7264fd956c0545cab8c0/system-control-with-label~dark%402x.png)
![A checkmark in a circle to indicate correct usage.](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)
![A partial screenshot showing an example of the Camera Control overlay with a slider control displaying a value without information about what the value represents.](https://docs-assets.developer.apple.com/published/ee13527a1983c79b04fc44392a8f03d6/system-control-no-label~dark%402x.png)
![An X in a circle to indicate incorrect usage.](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)
**Define prominent values for a slider control.** Prominent values are ones people choose most frequently, or values that are evenly spaced, like the major increments of zoom factor. When a person slides on the Camera Control to adjust a slider control, the system more easily lands on prominent values you define. For developer guidance, see [prominentValues](../AVFoundation/AVCaptureSlider/prominentValues-199dz.md).
**Make space for the overlay in the viewfinder.** The overlay and control labels occupy the screen area adjacent to the Camera Control in both portrait and landscape orientations. To avoid overlapping the interface elements of your camera capture experience, place your UI outside of the overlay areas. Maximize the height and width of the viewfinder and allow the overlay to appear and disappear over it.
![Partial screenshots showing the Camera Control overlay with its control's label in the viewport in portrait and landscape orientations on iPhone.](https://docs-assets.developer.apple.com/published/1ac20f6373076ebf55b8896368c6cb0b/camera-control-portrait-landscape-orientation~dark%402x.png)
**Minimize distractions in the viewfinder.** When capturing a photo or video, people appreciate a large preview image with as few visual distractions as possible. Avoid duplicating controls, like sliders and toggles, in your UI and the overlay when the system displays the overlay.
![A partial screenshot showing an example of the Camera Control overlay with UI elements removed from the capture viewport.](https://docs-assets.developer.apple.com/published/658850f8487ef5d1c8f49785003b764c/camera-control-screen-ui-good-example~dark%402x.png)
![A checkmark in a circle to indicate correct usage.](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)
![A partial screenshot showing an example of the Camera Control overlay with UI elements duplicated in the capture viewport.](https://docs-assets.developer.apple.com/published/80d2671546a6a1202fbd9d949e8f5545/camera-control-screen-ui-bad-example~dark%402x.png)
![An X in a circle to indicate incorrect usage.](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)
**Enable or disable controls depending on the camera mode.** For example, disable video controls when taking photos. The overlay supports multiple controls, but you can’t remove or add controls at runtime.
**Consider how to arrange your controls.** Order commonly used controls toward the middle to allow quick access, and include lesser used controls on either side. When a person lightly presses the Camera Control to open the overlay again, the system remembers the last control they used in your app.
**Allow people to use the Camera Control to launch your experience from anywhere.** Create a locked camera capture extension that lets people configure the Camera Control to launch your app’s camera experience from their locked device, the Home Screen, or from within other apps. For guidance, see [Camera experiences on a locked device](controls.md#Camera-experiences-on-a-locked-device).

## Platform considerations
*Not supported in iPadOS, macOS, watchOS, tvOS, or visionOS.*

## Resources

#### Related
[SF Symbols](sf-symbols.md)
[Controls](controls.md)

#### Developer documentation
[Enhancing your app experience with the Camera Control](../AVFoundation/enhancing-your-app-experience-with-the-camera-control.md) — AVFoundation
[AVCaptureControl](../AVFoundation/AVCaptureControl.md) — AVFoundation
[LockedCameraCapture](../LockedCameraCapture.md)

## Change log
| Date | Changes |
| --- | --- |
| September 9, 2024 | New page. |




---
*Source: [https://developer.apple.com/design/human-interface-guidelines/camera-control](https://developer.apple.com/design/human-interface-guidelines/camera-control)*
