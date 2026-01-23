---
url: https://developer.apple.com/design/human-interface-guidelines/photo-editing
framework: HIG
---

# Photo editing

**Type:** article

**Platforms:** ios, ipados, macos

Photo-editing extensions let people modify photos and videos within the Photos app by applying filters or making other changes.

![A sketch of crop marks surrounded by two arrows, suggesting photo editing. The image is overlaid with rectangular and circular grid lines and is tinted blue to subtly reflect the blue in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/77af5c44937ad338f3525de618498b97/technologies-photo-editing-intro~dark%402x.png)
Edits are always saved in the Photos app as new files, safely preserving the original versions.
To access a photo editing extension, a photo must be in edit mode. While in edit mode, tapping the extension icon in the toolbar displays an action menu of available editing extensions. Selecting one displays the extension’s interface in a modal view containing a top toolbar. Dismissing this view confirms and saves the edit, or cancels it and returns to the Photos app.

## Best practices
**Confirm cancellation of edits.** Editing a photo or video can be time consuming. If someone taps the Cancel button, don’t immediately discard their changes. Ask them to confirm that they really want to cancel, and inform them that any edits will be lost after cancellation. There’s no need to show this confirmation if no edits have been made yet.
**Don’t provide a custom top toolbar.** Your extension loads within a modal view that already includes a toolbar. Providing a second toolbar is confusing and takes space away from the content being edited.
**Let people preview edits.** It’s hard to approve an edit if you can’t see what it looks like. Let people see the result of their work before closing your extension and returning to the Photos app.
**Use your app icon for your photo editing extension icon.** This instills confidence that the extension is in fact provided by your app.

## Platform considerations
*No additional considerations for iOS, iPadOS, or macOS. Not supported in tvOS, visionOS, or watchOS.*

## Resources

#### Developer documentation
[App extensions](https://developer.apple.com/app-extensions/)
[PhotoKit](../PhotoKit.md)

#### Videos
- [Introducing Photo Segmentation Mattes](https://developer.apple.com/videos/play/wwdc2019/260) - Photos captured in Portrait Mode on iOS 12 contain an embedded person segmentation matte that made it easy to create creative visual effects like background replacement. iOS 13 leverages on-device machine learning to provide new segmentation mattes for any captured photo. Learn about the new semantic segmentation mattes available to you from both AVCapture and Core Image to isolate a person's hair, skin, and teeth. Using any of these individual mattes or combining all of them, your app can now offer a tremendous amount of photo editing control.



---
*Source: [https://developer.apple.com/design/human-interface-guidelines/photo-editing](https://developer.apple.com/design/human-interface-guidelines/photo-editing)*
