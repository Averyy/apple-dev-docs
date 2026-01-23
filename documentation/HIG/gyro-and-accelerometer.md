---
url: https://developer.apple.com/design/human-interface-guidelines/gyro-and-accelerometer
framework: HIG
---

# Gyroscope and accelerometer

**Type:** article

**Platforms:** ios, ipados, macos, tvos, visionos, watchos

On-device gyroscopes and accelerometers can supply data about a device’s movement in the physical world.

![A sketch of a gyroscope, suggesting movement. The image is overlaid with rectangular and circular grid lines and is tinted purple to subtly reflect the purple in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/39c8cae08431ef29f4594c828c6292b2/inputs-gyroscope-intro~dark%402x.png)
You can use accelerometer and gyroscope data to provide experiences based on real-time, motion-based information in apps and games that run in iOS, iPadOS, and watchOS. tvOS apps can use gyroscope data from the Siri Remote. For developer guidance, see [Core Motion](../CoreMotion.md).

## Best practices
**Use motion data only to offer a tangible benefit to people.** For example, a fitness app might use the data to provide feedback about people’s activity and general health, and a game might use the data to enhance gameplay. Avoid gathering data simply to have the data.

> **Important:** If your experience needs to access motion data from a device, you must provide copy that explains why. The first time your app or game tries to access this type of data, the system includes your copy in a permission request, where people can grant or deny access.
**Outside of active gameplay, avoid using accelerometers or gyroscopes for the direct manipulation of your interface.** Some motion-based gestures may be difficult to replicate precisely, may be physically challenging for some people to perform, and may affect battery usage.

## Platform considerations
*No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.*

## Resources

#### Related
[Feedback](feedback.md)

#### Developer documentation
[Getting processed device-motion data](../CoreMotion/getting-processed-device-motion-data.md) — Core Motion

#### Videos
- [Measure health with motion](https://developer.apple.com/videos/play/wwdc2021/10287) - Discover how you can take your app’s health monitoring to the next level with motion data. Meet Walking Steadiness for iPhone and the six-minute-walk metric for Apple Watch: Walking Steadiness can help your app interpret someone’s quality of walking and risk of falling, while the six-minute-walk metric — along with the HealthKit estimate recalibration API — can track changes to walking endurance following acute events like surgery. We’ll show you how you can support these metrics and help provide actionable health data to people who use your app, helping improve patient care and clinical trials, especially as more services must be delivered remotely.



---
*Source: [https://developer.apple.com/design/human-interface-guidelines/gyro-and-accelerometer](https://developer.apple.com/design/human-interface-guidelines/gyro-and-accelerometer)*
