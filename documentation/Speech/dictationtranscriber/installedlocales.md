# installedLocales

**Framework**: Speech  
**Kind**: property

The locales that the transcriber can transcribe into, considering only locales that are installed on the device.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
static var installedLocales: [Locale] { get async }
```

## See Also

- [static var supportedLocales: [Locale]](dictationtranscriber/supportedlocales.md)
  The locales that the transcriber can transcribe into, including locales that may not be installed but are downloadable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/dictationtranscriber/installedlocales)*