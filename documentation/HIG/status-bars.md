---
url: https://developer.apple.com/design/human-interface-guidelines/status-bars
framework: HIG
---

# Status bars

**Type:** article

**Platforms:** ios, ipados

A status bar appears along the upper edge of the screen and displays information about the device’s current state, like the time, cellular carrier, and battery level.

![A stylized representation of an iPhone status bar with labels showing the time and cellular, Wi-Fi, and battery levels. The image is tinted red to subtly reflect the red in the original six-color Apple logo.](/images/com.apple.HIG/components-status-bar-intro~dark@2x.png)

## Best practices
**Obscure content under the status bar.** By default, the background of the status bar is transparent, allowing content beneath to show through. This transparency can make it difficult to see information presented in the status bar. If controls are visible behind the status bar, people may attempt to interact with them and be unable to do so. Be sure to keep the status bar readable, and don’t imply that content behind it is interactive. Prefer using a scroll edge effect to place a blurred view behind the status bar. For developer guidance, see [ScrollEdgeEffectStyle](../swiftui/scrolledgeeffectstyle.md) and [UIScrollEdgeEffect](../uikit/uiscrolledgeeffect.md).
**Consider temporarily hiding the status bar when displaying full-screen media.** A status bar can be distracting when people are paying attention to media. Temporarily hide these elements to provide a more immersive experience. The Photos app, for example, hides the status bar and other interface elements when people browse full-screen photos.
![A screenshot of the top half of the Photos app on iPhone, showing a photo filling the screen. The status bar is visible at the top of the screen.](/images/com.apple.HIG/status-bar-visible@2x.png)
![A screenshot of the top half of the Photos app on iPhone, showing a photo filling the screen. The status bar is hidden, and only the photo is visible.](/images/com.apple.HIG/status-bar-hidden@2x.png)
**Avoid permanently hiding the status bar.** Without a status bar, people have to leave your app to check the time or see if they have a Wi-Fi connection. Let people redisplay a hidden status bar with a simple, discoverable gesture. For example, when browsing full-screen photos in the Photos app, a single tap shows the status bar again.

## Platform considerations
*No additional considerations for iOS or iPadOS. Not supported in macOS, tvOS, visionOS, or watchOS.*

## Resources

#### Developer documentation
[UIStatusBarStyle](../uikit/uistatusbarstyle.md) — UIKit
[preferredStatusBarStyle](../uikit/uiviewcontroller/preferredstatusbarstyle.md) — UIKit



---
*Source: [https://developer.apple.com/design/human-interface-guidelines/status-bars](https://developer.apple.com/design/human-interface-guidelines/status-bars)*
