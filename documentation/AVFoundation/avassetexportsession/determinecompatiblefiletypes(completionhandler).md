# determineCompatibleFileTypes(completionHandler:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Determines the output file types an asset export session supports writing in its current configuration.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func determineCompatibleFileTypes(completionHandler handler: @escaping @Sendable ([AVFileType]) -> Void)
```

```swift
var compatibleFileTypes: [AVFileType] { get async }
```

```objc
- (void) determineCompatibleFileTypesWithCompletionHandler:(void (^)(NSArray<NSString *> *compatibleFileTypes)) handler;
```

## Parameters

- `handler`: A callback the system passes an array of [`AVFileType`](../avfiletype.md) structures when it determines the compatible file types.

## See Also

### Accessing export presets
- [var presetName: String](./presetname.md)
  The name of the preset that the asset export session uses.
- [class func allExportPresets() -> [String]](./allexportpresets%28%29.md)
  Returns all available export preset names.
- [class func determineCompatibility(ofExportPreset: String, with: AVAsset, outputFileType: AVFileType?, completionHandler: (Bool) -> Void)](./determinecompatibility%28ofexportpreset,with,outputfiletype,completionhandler%29.md)
  Determines an export preset’s compatibility to export the asset in a container of the output file type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/determinecompatiblefiletypes(completionhandler:))*