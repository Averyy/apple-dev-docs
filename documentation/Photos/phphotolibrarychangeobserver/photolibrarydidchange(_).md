# photoLibraryDidChange(_:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells your observer that a set of changes has occurred in the Photos library.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func photoLibraryDidChange(_ changeInstance: PHChange)
```

```objc
- (void) photoLibraryDidChange:(PHChange *) changeInstance;
```

## Discussion

Use the provided [`PHChange`](../phchange.md) object to find out which, if any, of the albums or collections you’re interested in have changed and get detailed change information. Call the change object’s [`changeDetailsForObject:`](../phchange/changedetailsforobject_.md) method to get information about changes to an asset’s contents or metadata properties or about a collection’s metadata properties. Call the change object’s [`changeDetails(for:)`](../phchange/changedetails%28for%29-33a6n.md) to get information about changes to a collection’s list of members (or to any other fetch result).

Photos calls this method on an arbitrary queue. If you need to update your app’s UI as a result of the change, dispatch to the main queue.

## Parameters

- `changeInstance`: An object representing the changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotolibrarychangeobserver/photolibrarydidchange(_:))*