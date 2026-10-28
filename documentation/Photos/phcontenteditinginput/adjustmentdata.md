# adjustmentData

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

An object that describes the most recent edit to the asset’s content.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var adjustmentData: PHAdjustmentData? { get }
```

```objc
@property (strong, readonly, nullable) PHAdjustmentData * adjustmentData;
```

## Discussion

Adjustment data describes the “recipe” for the last edit made to an asset’s photo or video content. For example, a photo editing app can use this property to read information about a set of filters applied to a photo. With this information, your app can later allow a user to change the filter parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcontenteditinginput/adjustmentdata)*