# Optimizing iPhone and iPad apps to support ProMotion displays

**Framework**: Core Animation

Improve your app’s visual appearance and save power by requesting preferred refresh rates and synchronizing your animations with the system.

#### Overview

ProMotion displays are capable of dynamically switching between frame rates ranging from 24Hz to 120Hz on iPad Pro, and from 10Hz to 120Hz on supported iPhone devices. Your app can present smooth, seamless animations and take advantage of power-saving opportunities in ProMotion displays. Devices with a ProMotion display include:

| iPhone | iPad |
| --- | --- |
| iPhone Air | iPad Pro 11-inch |
| iPhone 17 and later | iPad Pro 13-inch |
| iPhone 13 Pro and later | iPad Pro 12.9-inch (2nd generation and later) |
| iPhone 13 Pro Max and later | iPad Pro 10.5-inch |

Your app may already be capable of taking advantage of these new refresh rates without any changes. Some framework animation features handle frame pacing automatically for you, including:

- [`UIKit`](https://developer.apple.com/documentation/UIKit)
- [`SwiftUI`](https://developer.apple.com/documentation/SwiftUI)
- [`CAAnimation`](caanimation.md)
- [`SpriteKit`](https://developer.apple.com/documentation/SpriteKit)

If your app needs to provide animated content with special timing, you can use [`CADisplayLink`](cadisplaylink.md) to synchronize your drawing code with the display refresh. In the following code example, a `DisplayLinkManager` class handles frame updates by creating and activating a display link:

```swift
class DisplayLinkManager {
    var displayLink: CADisplayLink?
    
    // Perform your custom animation in a callback function.
    @objc func displayLinkCallback(sender: CADisplayLink) {
        //...
    }
    
    func createDisplayLink() {
        // Create the display link.
        displayLink = CADisplayLink(target: self, selector: #selector(displayLinkCallback))

        // You can configure the display link before activating it.

        // Activate your display link by adding it to the main runloop.
        displayLink.add(to: .current, forMode: .default)
    }
}
```

You can provide timing hints for any `CAAnimation` animation in an app that needs special timing to improve visual appearance or save power. For more information on refresh rates, watch WWDC21 [`Session 10147: Optimize for variable refresh rate displays`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2021/10147/).

#### Understand Refresh Rates

ProMotion displays behave differently than a traditional display. The system insulates the ProMotion display’s actual refresh rate from your app — you can’t force a ProMotion display to show your content at any specific rate.

From your app’s point of view, the refresh rate for a ProMotion display is the rate that Core Animation renders the content for the entire display. The system synchronizes the rendering process with the display hardware’s refresh rate, but the display hardware doesn’t necessarily drive the rendering process.

Core Animation arbitrates the animations it presents onscreen and determines the refresh rate at any particular time. Your app can provide hints to Core Animation about what refresh rates the app prefers for its animations. Take advantage of power-saving opportunities by using lower refresh rates whenever possible. Higher refresh rates can result in significant power consumption.

Devices with a ProMotion display can present content using the following refresh rates and timings:

| Refresh rate and timing | iPhone | iPad Pro |
| --- | --- | --- |
| 120Hz (8ms) | ✅ | ✅ |
| 80Hz (12ms) | ✅ |  |
| 60Hz (16ms) | ✅ | ✅ |
| 48Hz (20ms) | ✅ |  |
| 40Hz (25ms) | ✅ | ✅ |
| 30Hz (33ms) | ✅ | ✅ |
| 24Hz (41ms) | ✅ | ✅ |
| 20Hz (50ms) | ✅ |  |
| 16Hz (62ms) | ✅ |  |
| 15Hz (66ms) | ✅ |  |
| 12Hz (83ms) | ✅ |  |
| 10Hz (100ms) | ✅ |  |

Display refresh rates can change for many reasons and your app can’t presume a specific refresh rate at any time.

Custom animations in your app need to adapt to changes in refresh rates. For example, the system disables faster refresh rates in low power mode or if a device gets hot. Also, while UIKit and Core Animation are managing various GUI elements, Core Animation might elect to vary the refresh rate to provide an enhanced user experience.

#### Enable Faster Promotion Refresh Rates

The device doesn’t apply your preferred refresh rates unless you unlock the full range of frame rates. Specifically, Core Animation won’t apply any refresh rate that’s faster than the system’s default. To enable your [`preferredFrameRateRange`](cadisplaylink/preferredframeraterange.md) timing hints for [`CADisplayLink`](cadisplaylink.md) callbacks and [`CAAnimation`](caanimation.md) animations in your iPhone app, use the Info pane in Xcode to add the `CADisableMinimumFrameDurationOnPhone` key to your app’s information property list with the Boolean value `true`:

```plist
<key>CADisableMinimumFrameDurationOnPhone</key><true/>
```

If you don’t enable this support, Core Animation won’t access higher frame rates (above 60Hz). In these cases, other animations or GUI operations may affect the rate at which Core Animation calls your `CADisplayLink` callback. The iPad Pro doesn’t require this special configuration.

#### Provide Time Paced Content to a Promotion Display

The system automatically handles frame pacing for UIKit, SpriteKit, SwiftUI, and [`CAAnimation`](caanimation.md) animations for you. When your app needs to present custom content accurately, provide hints about your app’s preferred refresh rate to [`CADisplayLink`](cadisplaylink.md) or `CAAnimation`.

> ❗ **Important**:  Prepare your app to operate at any refresh rate, not just those it requests through `CADisplayLink` or `CAAnimation`.

When specifying a preferred frame rate, specify the best possible frame rate for your content. `CADisplayLink` might be unable to update the display at that rate at all times, but it attempts to provide the closest refresh rate possible, given available hardware and current conditions on the device.

In iOS 15 and later, the system provides games with special priority to 30Hz and 60Hz refresh rates to ensure optimal performance. To access this special prioritization, your game needs to set a [`preferredFrameRateRange`](cadisplaylink/preferredframeraterange.md) with a [`CAFrameRateRange`](caframeraterange.md) structure using one or both of those values, as shown here:

```swift
// 30Hz and 60Hz refresh rates are given special priority
let prioritizedFrameRateRange = CAFrameRateRange(minimum: 30,
                                                maximum: 60,
                                                preferred: 60)
displayLink.preferredFrameRateRange = prioritizedFrameRateRange
```

Use system resources efficiently by limiting the number of display links in your app to the minimum required to accomplish your goals. Group animations with similar timings together in one `CADisplayLink` even if they are in different views.

> ❗ **Important**:  Don’t use timers or other strategies that don’t properly align with the Core Animation display refresh cycle.

#### Provide Timing Hints to Core Animation

Apps that use the [`CADisplayLink`](cadisplaylink.md) and [`CAAnimation`](caanimation.md) APIs can provide hints about the refresh rates they prefer, and Core Animation attempts to accommodate these preferences. Your app must not assume that Core Animation calls your `CADisplayLink` callback at any specific refresh rate or even at the rate requested.

In iOS 14 and earlier, you provide the preferred refresh rate by setting the [`preferredFramesPerSecond`](cadisplaylink/preferredframespersecond.md) property.

```swift
func createDisplayLink() {
    // Create the display link.
    displayLink = CADisplayLink(target: self, selector: #selector(displayLinkCallback))
    
    // In iOS 14 and earlier, configure your desired refresh rate
    // by setting the `preferredFramesPerSecond` property.
    displayLink?.preferredFramesPerSecond = 30
    
    // Activate your `CADisplayLink` by adding it to the main runloop.
    displayLink?.add(to: .current, forMode: .default)
}
```

In iOS 15 and later, you set a [`preferredFrameRateRange`](cadisplaylink/preferredframeraterange.md) by adding the [`CAFrameRateRange`](caframeraterange.md) structure and setting the [`minimum`](caframeraterange/minimum.md), [`maximum`](caframeraterange/maximum.md), and [`preferred`](caframeraterange/preferred-7l3ki.md) refresh rates for your app, as shown here:

```swift
func createDisplayLink() {
    // Create the display link.
    displayLink = CADisplayLink(target: self, selector: #selector(displayLinkCallback))

    // In iOS 15 and later, configure your desired refresh rate
    // with a `preferredFrameRateRange`.
    displayLink?.preferredFrameRateRange = CAFrameRateRange(minimum: 10,
                                                            maximum: 60,
                                                            preferred: 30)
    
    // Activate your `CADisplayLink` by adding it to the main runloop.
    displayLink?.add(to: .current, forMode: .default)
}
```

The following table provides some suggested frame rate hints for different types of animations:

| Animation Type | Examples from iOS | Frame Rate Ranges | Notes |
| --- | --- | --- | --- |
| High-impact animations | Tapping an item in a grid to expand to fullscreen, such as in the Photos app; first-person, full-motion gaming experience; or sheet presentation | `CAFrameRateRange(minimum:80, maximum:120, preferred:120)` | Use sparingly to minimize power consumption |
| Alpha or color transitions; small movements | Switch or control changing state; progress spinner; blurring a background | [`CAFrameRateRange`](caframeraterange.md).[`default`](caframeraterange/default.md) | No need for a higher frame rate for the same visual effect |
| Small, low-speed animations | Clock ticking; progress bar | `CAFrameRateRange(minimum:8, maximum:15, preferred:0),`  ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `CAFrameRateRange(minimum:15, maximum:24, preferred:0),`, or  ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `CAFrameRateRange(minimum:30, maximum:48, preferred:0)` | Looks good at slow speeds; power-saving opportunities |
| All other cases |  | [`CAFrameRateRange`](caframeraterange.md).[`default`](caframeraterange/default.md) |  |

For a fluid appearance, fast-moving objects that travel across the screen benefit from having a higher refresh rate. Whereas, smaller movements — like an icon that rotates in-place — may look just fine at a lower rate. To save energy, choose the lowest frame rate that achieve’s your desired visual flow.

> **Note**:  Be selective when requesting the maximum frame rate. If your animation requests 120Hz but can’t keep up, it may render poorly. But the same animation may be able to maintain a steady cadence at a lower rate.

Use these recommended timings and principles when designing and building your app, but also do your own testing on an actual device to make sure your animations look good.

#### Synchronize Your Content with the Display

Core Animation reports timing information about the current refresh interval in the [`timestamp`](cadisplaylink/timestamp.md) and [`targetTimestamp`](cadisplaylink/targettimestamp.md) properties each time it calls your app’s [`CADisplayLink`](cadisplaylink.md) callback. When Core Animation calls your `CADisplayLink` callback, `timestamp` equals the beginning of the current refresh interval and `targetTimestamp` is equal to the end of the interval. When providing new content, `targetTimestamp` is your deadline to submit changes for the next frame that Core Animation renders to the device’s display.

> ❗ **Important**:  Always use `targetTimestamp` to drive any animation, physics, or other time-related content provided in your `CADisplayLink` callback.

While `timestamp` reflects the time of the beginning of the current refresh interval, there might be some latency between that time and the time when Core Animation calls your `CADisplayLink` callback. To calculate how much time your `CADisplayLink` callback has to prepare content before `targetTimestamp`, subtract the value returned by [`CACurrentMediaTime()`](cacurrentmediatime().md) from `targetTimestamp`. This example `CADisplayLink` callback calculates the available time to prepare updates for the next frame:

```swift
// Calculate the working time available to the `CADisplayLink` callback.
@objc func displayLinkCallback(sender: CADisplayLink) {
    // At this moment in time, there are `workingTime` seconds available to
    // generate content for the next frame, so Core Animation can render
    // it to the display.
    let workingTime = sender.targetTimestamp - CACurrentMediaTime()
    //...
}
```

> ❗ **Important**:  Lengthy callback execution times can prevent refresh intervals from receiving `CADisplayLink` callbacks.

If the completion time for a `CADisplayLink` callback exceeds the `targetTimestamp`, the next refresh interval doesn’t receive a callback. The next time Core Animation invokes your `CADisplayLink` callback, provide recovery for this condition to ensure proper display synchronization with your content.

> 💡 **Tip**:  Synchronize your animations with other Core Animation or UIKit animations using [`presentsWithTransaction`](cametallayer/presentswithtransaction.md).

#### Test and Validate Display Performance

To improve your app’s synchronization with the display, test frame rate changes under different system conditions. Any changes made to the frame rate hints provided to [`CADisplayLink`](cadisplaylink.md) take effect in the next `CADisplayLink` callback.

Use this capability of the API to test how your app responds to changing refresh rates mid-flight. While your app is running, provide different frame rate hints by setting the [`preferredFrameRateRange`](cadisplaylink/preferredframeraterange.md) method’s `maximum`, `minimum`, and `preferred` properties to the same value.

Create `CADisplayLink` callback tests for different refresh conditions, for example:

- Ensure the `CADisplayLink` callback operates correctly at all refresh rates allowed by ProMotion displays.
- Verify the `CADisplayLink` callback is capable of handling gradual frame rate changes as well as sudden changes.
- Make sure your `CADisplayLink` callback isn’t cycling the device in and out of thermal mode and causing frame rate changes due to thermal conditions. When a device overheats, the system may respond by reducing the frame rate.

> ❗ **Important**:  You can avoid undesirable power conditions by maintaining a consistent drawing quality. Dynamically adjusting render quality in response to refresh rates in your `CADisplayLink` callback can throttle the GPU. To avoid an oscillating feedback loop, use code paths for different frame rates and test them on actual devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/optimizing-iphone-and-ipad-apps-to-support-promotion-displays)*