# iconURL(fitting:)

**Framework**: ManagedAppDistribution  
**Kind**: method

A URL for the icon of the app.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- visionOS 2.4+

## Declaration

```swift
func iconURL(fitting size: CGSize) -> URL?
```

#### Return Value

The URL of the icon.

#### Discussion

The icon scales to fit the given size.

## Parameters

- `size`: The size of the icon.

## See Also

- [let name: String](managedapp/name.md)
  The app’s localized name.
- [let subtitle: String?](managedapp/subtitle.md)
  The app’s localized subtitle.
- [let description: String?](managedapp/description.md)
  The app’s localized description.
- [let fileSize: Measurement<UnitInformationStorage>?](managedapp/filesize.md)
  The size of the app in bytes.
- [func screenshotURLs(fitting: CGSize) -> [URL]](managedapp/screenshoturls(fitting:).md)
  An array of the app’s screenshot URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedapp/iconurl(fitting:))*