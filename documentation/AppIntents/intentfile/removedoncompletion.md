# removedOnCompletion

**Framework**: App Intents  
**Kind**: property

Indicates whether the file should be automatically deleted from disk when the Shortcut is done running. `false` by default.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
var removedOnCompletion: Bool { get set }
```

## See Also

- [var filename: String](intentfile/filename.md)
  The human-readable name of the file, which will be displayed to the user.
- [var fileURL: URL?](intentfile/fileurl.md)
  URL to the file on disk, if any. If the file isn’t stored on disk, access the contents using the `data` property.
- [var type: UTType?](intentfile/type.md)
  The uniform type identifier of the file. (i.e. “public.json”, “public.png”, or any custom type) More information about uniform type identifiers can be found in <CoreServices/UTCoreTypes.h>
- [var data: Data](intentfile/data.md)
  The contents of the file. If the file was created with a URL, accessing this property will memory map the file contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentfile/removedoncompletion)*