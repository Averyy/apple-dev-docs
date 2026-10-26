# supportedExtensionAvailable

**Framework**: AVSystemRouting  
**Kind**: property  
**Role**: Type Property

A Boolean value that indicates whether a supported system routing extension is available.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
@property (class, nonatomic, readonly, getter=isSupportedExtensionAvailable) BOOL supportedExtensionAvailable;
```

#### Discussion

This property is `YES` when the app has declared support for at least one form of system routing in its `Info.plist` and a matching extension is installed:

- one or more protocols listed under `MDESupportedProtocols` and at least one installed extension matches, or
- `MDESupportsUniversalURLPlayback` set to `true`, with an installed extension that supports URL playback.

If neither key is declared, or no installed extension matches the declared support, this property is `NO`.

Check this property before attempting to use the routing controller to ensure that the necessary system support is available for your app’s routing requirements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroutecontroller-4teia/supportedextensionavailable)*