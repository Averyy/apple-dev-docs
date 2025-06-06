# hlg

**Framework**: Core Animation  
**Kind**: property

Extended dynamic range (EDR) metadata for the Hybrid Log-Gamma (HLG) transfer function.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class var hlg: CAEDRMetadata { get }
```

#### Discussion

Your content should be scene referred and encoded with the ITU-R BT.2100-2 Hybrid Log Gamma (HLG) opto-electrical transfer function (OETF). The system applies the opto-optical transfer function (OOTF) based on peak display brightness and ambient lighting. If you’re rendering to a [`CAMetalLayer`](cametallayer.md) with a linear colorspace (for floating point EDR layers), you must apply the HLG inverse OETF without normalization, to provide a nominal range of `[0, 12]`.

For more information on HLG, see [`https://www.itu.int/rec/R-REC-BT.2100`](https://developer.apple.comhttps://www.itu.int/rec/R-REC-BT.2100).


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caedrmetadata/hlg)*