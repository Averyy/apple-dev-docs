# supportedExtensionAvailable

**Framework**: AVSystemRouting  
**Kind**: property

A Boolean value that indicates whether a supported system routing extension is available.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
final class var supportedExtensionAvailable: Bool { get }
```

#### Discussion

This property is `true` when the app has declared support for at least one form of system routing in its `Info.plist` and a matching extension is installed:

- one or more protocols listed under `MDESupportedProtocols` and at least one installed extension matches, or
- `MDESupportsUniversalURLPlayback` set to `true`, with an installed extension that supports URL playback.

If neither key is declared, or no installed extension matches the declared support, this property is `false`.

Check this property before attempting to use the routing controller to ensure that the necessary system support is available for your app’s routing requirements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroutecontroller-18ns8/supportedextensionavailable)*