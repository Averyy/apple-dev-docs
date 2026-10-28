# iconURL(fitting:)

**Framework**: ManagedAppDistribution  
**Kind**: method  
**Role**: Instance Method

A URL for the icon of the app.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 2.4+

## Declaration

```swift
func iconURL(fitting size: CGSize) -> URL?
```

## Return Value

The URL of the icon.

## Discussion

The icon scales to fit the given size.

## Parameters

- `size`: The size of the icon.

## See Also

### Obtaining general information
- [let name: String](./name.md)
  The app’s localized name.
- [let subtitle: String?](./subtitle.md)
  The app’s localized subtitle.
- [let description: String?](./description.md)
  The app’s localized description.
- [let fileSize: Measurement<UnitInformationStorage>?](./filesize.md)
  The size of the app in bytes.
- [func screenshotURLs(fitting: CGSize) -> [URL]](./screenshoturls%28fitting%29.md)
  An array of the app’s screenshot URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedapp/iconurl(fitting:))*