# supportedLocales

**Framework**: Speech  
**Kind**: property

The locales that the transcriber can transcribe into, including locales that may not be installed but are downloadable.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static var supportedLocales: [Locale] { get async }
```

#### Discussion

This array is empty if the device does not support the transcriber.

## See Also

- [static var installedLocales: [Locale]](speechtranscriber/installedlocales.md)
  The locales that the transcriber can transcribe into, considering only locales that are installed on the device.
- [static func supportedLocale(equivalentTo: Locale) async -> Locale?](speechtranscriber/supportedlocale(equivalentto:).md)
  A locale from the module’s supported locales equivalent to the given locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechtranscriber/supportedlocales)*