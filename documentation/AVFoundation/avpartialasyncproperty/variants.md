# variants

**Framework**: AVFoundation  
**Kind**: property

An array of variants that an asset contains.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var variants: AVAsyncProperty<Root, [AVAssetVariant]> { get }
```

#### Discussion

Use the [`load(_:isolation:)`](avasynchronouskeyvalueloading/load(_:isolation:).md) method to retrieve the property value.

Some variants may not be playable according to the current device configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/variants)*