# Optimizing ProMotion refresh rates for iPhone 13 Pro and iPad Pro

**Framework**: Core Animation

Provide custom animated content for ProMotion displays.

#### Overview

The iPhone 13 Pro, the iPhone 13 Pro Max, and the iPad Pro ProMotion displays are capable of dynamically switching between:

- Faster refresh rates up to 120Hz
- Slower refresh rates down to 24Hz or 10Hz

This dynamic switching means your app can present smooth, seamless animations and take advantage of power-saving opportunities. Your app may already be capable of taking advantage of these new refresh rates without any changes. Some framework animation features handle frame pacing automatically for you, including:

- [`UIKit`](https://developer.apple.com/documentation/UIKit)
- [`SwiftUI`](https://developer.apple.com/documentation/SwiftUI)
- [`SpriteKit`](https://developer.apple.com/documentation/SpriteKit)
- [`CAAnimation`](caanimation.md)

If your app needs to provide animated content with special timing, you can use Core Animation’s [`CADisplayLink`](cadisplaylink.md). You can provide timing hints for any CAAnimation-based animation in an app that needs special timing to improve visual appearance or save power. For more information on refresh rates, see WWDC21 - [`Session 10147: Optimize for variable refresh rate displays`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2021/10147/).

> ❗ **Important**:  Use lower refresh rates whenever possible to save power, because higher refresh rates can result in significant power consumption.

##### Understand Refresh Rates

You can’t force a ProMotion display to show your content at any specific rate. The refresh rate of a ProMotion display behaves differently than a traditional display. The system insulates the ProMotion’s actual refresh rate from your app. From your app’s point of view, the refresh rate for a ProMotion display is the rate that Core Animation renders the content for the entire display. The system synchronizes the rendering process with the display hardware’s refresh rate, but the display hardware doesn’t necessarily drive the rendering process. Core Animation arbitrates all the animations it presents on the screen and determines the refresh rate at any particular time. Your app can provide hints to Core Animation about what refresh rates the app prefers for its animations.

The iPhone 13 Pro and iPhone 13 Pro Max ProMotion displays can present content on the display using the following refresh rates and timings:

- 120Hz (8ms)
- 80Hz (12ms)
- 60Hz (16ms)
- 48Hz (20ms)
- 40Hz (25ms)
- 30Hz (33ms)
- 24Hz (41ms)
- 20Hz (50ms)
- 16Hz (62ms)
- 15Hz (66ms)
- 12Hz (83ms)
- 10Hz (100ms)

The iPad Pro’s ProMotion display can present content on the display using the following refresh rates and timings:

- 120Hz (8ms)
- 60Hz (16ms)
- 40Hz (25ms)
- 30Hz (33ms)
- 24Hz (41ms)

> ❗ **Important**:  Custom animations in your app need to be able to adapt to changes in refresh rates. Display refresh rates can change for many reasons and your app must not presume any specific refresh rate, at any time. For example, the system disables faster refresh rates in low power mode or if a device gets hot. Also, while UIKit and Core Animation are managing various GUI elements, Core Animation might elect to vary the refresh rate to provide an enhanced user experience.

##### Enable Faster Promotion Refresh Rates

If you don’t enable faster refresh rates for your app, your [`CADisplayLink`](cadisplaylink.md) callback might run at any of the speeds that the ProMotion display supports, at different times during normal GUI operations. In these cases, other animations in the system may affect the rate at which Core Animation calls your [`CADisplayLink`](cadisplaylink.md) callback. The rate at which Core Animation calls your [`CADisplayLink`](cadisplaylink.md) callback may not match the refresh rate hints that you provide to your [`CADisplayLink`](cadisplaylink.md) callback. Specifically, Core Animation won’t unlock any refresh rate that’s faster than the system’s default.

On iPhone 13 Pro or iPhone 13 Pro Max, add the following key to your `Info.plist` file to enable the full range of refresh rates for [`CADisplayLink`](cadisplaylink.md) callbacks and [`CAAnimation`](caanimation.md) animations in your app:

```plist
<key>CADisableMinimumFrameDurationOnPhone</key><true/>
```

Your app must use this key to access higher frame rates (above 60Hz) it sets in the [`preferredFrameRateRange`](cadisplaylink/preferredframeraterange.md) hint API. The iPad Pro doesn’t require this special configuration.

##### Provide Time Paced Content to a Promotion Display

The system automatically handles frame pacing for UIKit, SpriteKit , SwiftUI, and CAAnimation animations for you. When your app needs to present custom content accurately, provide hints about your app’s preferred refresh rate(s) to [`CADisplayLink`](cadisplaylink.md) or [`CAAnimation`](caanimation.md).

> ❗ **Important**:  Prepare your app to operate at any refresh rate, not just those it requests through [`CADisplayLink`](cadisplaylink.md) or [`CAAnimation`](caanimation.md).

When specifying a preferred frame rate, specify the best possible frame rate for your content. [`CADisplayLink`](cadisplaylink.md) might be unable to update the display at that rate at all times, but it attempts to provide the closest refresh rate as possible, given available hardware and current conditions on the device. iOS 15 provides special priority to 30Hz and 60Hz refresh rates (if your app provides hints that request either of these rates) to help with early adoption for game developers. This prioritization is specific to iOS 15.

> ❗ **Important**:  Don’t use timers or other strategies that don’t properly align with Core Animation’s display refresh cycle.

##### Provide Timing Hints to Core Animation

Apps that use the [`CADisplayLink`](cadisplaylink.md) and [`CAAnimation`](caanimation.md) APIs can provide hints about the refresh rates they prefer, and Core Animation attempts to accommodate these preferences. Your app must not assume that Core Animation calls your [`CADisplayLink`](cadisplaylink.md) callback at any specific refresh rate or even at the rate requested. Prior to iOS 15, you provide your preferred refresh rate by setting the [`preferredFramesPerSecond`](cadisplaylink/preferredframespersecond.md) property. This property means your app can specify its preferred refresh rate. In iOS 15, you can set a preferred [`preferredFrameRateRange`](cadisplaylink/preferredframeraterange.md) by using a [`CAFrameRateRange`](caframeraterange.md), which means you can set the [`minimum`](caframeraterange/minimum.md), [`maximum`](caframeraterange/maximum.md), and [`preferred`](caframeraterange/preferred-7l3ki.md) refresh rate for your content.

The following table provides some suggested frame rate hints for different types of animations:

|  |  |  |  |
| --- | --- | --- | --- |
| High-impact animations | Tapping an item in a grid to expand to fullscreen, such as in Photos.app; First-person, full-motion gaming experience; or Sheet Presentation | `CAFrameRateRange(minimum:80, maximum:120, preferred:120)` | Use sparingly to minimize power consumption |
| Alpha/Color transitions Small movements | Switch or control changing state; progress spinner; blurring a background | [`CAFrameRateRange`](caframeraterange.md).[`default`](caframeraterange/default.md) | No need for a higher frame rate for same visual effect |
| Small, low-speed animations | Clock ticking; progress bar | `CAFrameRateRange(minimum:8, maximum:15, preferred:0),`  ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `CAFrameRateRange(minimum:15, maximum:24, preferred:0), or`  ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `CAFrameRateRange(minimum:30, maximum:48, preferred:0)` | Looks good at slow speeds; power-saving opportunities |
| All other cases |  | [`CAFrameRateRange`](caframeraterange.md).[`default`](caframeraterange/default.md) |  |

As a general rule, for better visual appearance use faster refresh rates when animating fast-moving items that travel across large areas of the screen. But, if you’re animating a smaller item that doesn’t move over a great distance, but “animates in place”, that typically doesn’t benefit from a high refresh rate. You can use slower refresh rates when animating smaller items without any impact to the visual appearance. Selecting the right animation speed is always a tradeoff between a smoother visual appearance and saving energy. As a guiding principle, strive for the lowest animation speed possible while maintaining good visual appearance.

> ❗ **Important**:  Be selective when requesting the maximum frame rate. If your animation requests 120Hz but can’t keep up, it may render poorly. But the same animation may be able to maintain a steady cadence at a lower rate.

Use these recommended timings and principles when designing and building your app, but also do your own testing on an actual device to make sure your animations look good.

##### Synchronize Your Content with the Display

Core Animation reports timing information about the current refresh interval in the [`timestamp`](cadisplaylink/timestamp.md) and [`targetTimestamp`](cadisplaylink/targettimestamp.md) properties each time it calls your app’s [`CADisplayLink`](cadisplaylink.md) callback. When Core Animation calls your [`CADisplayLink`](cadisplaylink.md) callback , [`timestamp`](cadisplaylink/timestamp.md) equals the beginning of the current refresh interval and [`targetTimestamp`](cadisplaylink/targettimestamp.md) is equal to the end of the interval. When providing new content, [`targetTimestamp`](cadisplaylink/targettimestamp.md) is your deadline to submit changes for the next frame that Core Animation renders to the device’s display.

> ❗ **Important**:  Always use [`targetTimestamp`](cadisplaylink/targettimestamp.md) to drive any animation, physics, or other time-related content provided in your [`CADisplayLink`](cadisplaylink.md) callback.

Though [`timestamp`](cadisplaylink/timestamp.md) reflects the time of the beginning of the current refresh interval, there might be some latency between that time and the time when Core Animation calls your [`CADisplayLink`](cadisplaylink.md) callback. To calculate how much time your [`CADisplayLink`](cadisplaylink.md) callback has to prepare content before [`targetTimestamp`](cadisplaylink/targettimestamp.md), subtract the value returned by [`CACurrentMediaTime()`](cacurrentmediatime().md) from [`targetTimestamp`](cadisplaylink/targettimestamp.md). For example:

```swift
// Calculate the working time available to the `CADisplayLink` callback.
displayLink = CADisplayLink(target: self, selector: #selector(displayLinkCallback))

// Configure your desired refresh rate calling setPreferredFramesPerSecond
// or preferredFrameRateRange, then activate your CADisplayLink by adding it
// to the main runloop.
displayLink.add(to: .current, forMode: .default)

@objc func displayLinkCallback() {
    let workingTime = displayLink.targetTimestamp - CACurrentMediaTime()
    // At this moment in time, there are `workingTime` seconds available to
    // generate content for the next frame, so
    // Core Animation can render it to the display.
}
```

> ❗ **Important**:  If your [`CADisplayLink`](cadisplaylink.md) callback continues to execute past the [`targetTimestamp`](cadisplaylink/targettimestamp.md), then any refresh intervals with which your callback’s execution time overlaps don’t receive [`CADisplayLink`](cadisplaylink.md) callbacks. In these cases, you need to provide recovery for this condition in your code the next time Core Animation invokes your [`CADisplayLink`](cadisplaylink.md) callback, to ensure proper display synchronization with your content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/optimizing-promotion-refresh-rates-for-iphone-13-pro-and-ipad-pro)*