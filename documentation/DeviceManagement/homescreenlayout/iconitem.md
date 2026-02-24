# HomeScreenLayout.IconItem

**Framework**: Device Management  
**Kind**: dictionary

An array of dictionaries that conform to the icon dictionary format.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- tvOS 11.0+

## Declaration

```swift
object HomeScreenLayout.IconItem
```

## Properties

- `BundleID` (string): The bundle identifier of the app. This setting is required if the type is `Application`.
- `DisplayName` (string): The human-readable string shown to the user. This setting is valid only if the type is `Folder`.
- `Pages` ([[HomeScreenLayout.IconItem]]): An array of arrays of dictionaries, each conforming to the icon dictionary format. This setting is valid only if the type is `Folder`.
- `Type` (string) *(required)*: The type of the Dock item.
- `URL` (string): The URL of the existing web clip for this item. This setting is required if `type` is `WebClip`. If more than one web clip exists with the same URL, the behavior is undefined. Specifying a web clip in this payload doesn’t create the web clip. Use the [`WebClip`](webclip.md) payload to create a web clip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/homescreenlayout/iconitem)*