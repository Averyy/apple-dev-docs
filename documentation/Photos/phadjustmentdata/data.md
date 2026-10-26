# data

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

Data that contains the information necessary to reconstruct the adjustment.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var data: Data { get }
```

```objc
@property (strong, readonly) NSData * data;
```

#### Discussion

Use this property to resume working with the last edit that was made to an asset. For example, if your app applies Core Image filters to photos, this property may hold a serialized property list that describes the filters and their parameters. Use the [`formatIdentifier`](./formatidentifier.md) and [`formatVersion`](./formatversion.md) properties to determine whether the adjustment data saved with an asset is in a format that your app can understand.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phadjustmentdata/data)*