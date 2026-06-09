# openFileSystemExtensionsSettings()

**Framework**: FSKit  
**Kind**: method

Opens the File System Extensions settings in System Settings.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func openFileSystemExtensionsSettings() -> Bool
```

#### Return Value

`true` (Swift) or `YES` (Obj-C) if the settings were successfully opened; otherwise, `false` (Swift) or `NO`(Obj-C).

#### Discussion

Calling this method allows someone using your app to navigate to the File System Extensions pane in System Settings. From this pane, they can view, enable, and disable file system extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsclient/openfilesystemextensionssettings())*