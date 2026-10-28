# NSPhotoLibraryUsageDescription

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A message that tells people why the app is requesting access to their photo library.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- macOS 10.14+
- visionOS 1.0+

## Details

- **Name**: `NSPhotoLibraryUsageDescription` (Privacy - Photo Library Usage Description)
- **Type**: string

## Mentions

- [Requesting Authorization for Media Capture on macOS](../requesting-authorization-for-media-capture-on-macos.md)

## Discussion

If your app only adds assets to the photo library and does not read assets, use the  [`NSPhotoLibraryAddUsageDescription`](./nsphotolibraryaddusagedescription.md) key instead.

> ❗ **Important**:  This key is required if your app uses APIs that have read or write access to the user’s photo library.

## See Also

### Photos
- [Delivering an Enhanced Privacy Experience in Your Photos App](../../PhotoKit/delivering-an-enhanced-privacy-experience-in-your-photos-app.md)
  Adopt the latest privacy enhancements to deliver advanced user-privacy controls.
- [NSPhotoLibraryAddUsageDescription](./nsphotolibraryaddusagedescription.md)
  A message that tells people why the app is requesting add-only access to their photo library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsphotolibraryusagedescription)*