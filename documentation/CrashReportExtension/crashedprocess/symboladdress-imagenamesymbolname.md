# symbolAddress(imageName:symbolName:)

**Framework**: CrashReportExtension  
**Kind**: method

Looks up a symbol’s address by name.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
final func symbolAddress(imageName: String?, symbolName: String) -> UInt64
```

#### Return Value

The symbol’s address, or `0` if searching the image didn’t find the symbol.

## Parameters

- `imageName`: The path of the Mach-O binary image, such as `/usr/lib/libSystem.B.dylib`, that contains the symbol. Use `nil` to search for the symbol in all images loaded in the process space.
- `symbolName`: The name of the symbol to find.


---

*[View on Apple Developer](https://developer.apple.com/documentation/crashreportextension/crashedprocess/symboladdress(imagename:symbolname:))*