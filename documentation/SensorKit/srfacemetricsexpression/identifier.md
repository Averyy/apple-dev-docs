# identifier

**Framework**: SensorKit  
**Kind**: property

An identifier for the facial expression.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
var identifier: String { get }
```

#### Discussion

The possible values for a partial facial expression are:

| Identifier | Partial facial expression |
| --- | --- |
| `85E97F41-0CF7-481E-B9ED-8E5A90B4A547` | Inner brow raise |
| `5A3CBD39-B24F-463A-990C-18C5372D6F1B` | Brow raise with furrow |
| `D0859030-4703-45F6-A902-7634984A2074` | Brow raise without furrow |
| `A29952D5-F6EA-4562-9A12-43284B1DB634` | Brow furrow |
| `A8B47A8D-A86F-4159-8472-33C67D6250B5` | Mouth corner depress |
| `60A8B7A9-8C8F-401A-A8C4-C996B1397CC9` | Mouth stretch |
| `E5A9652C-9CF9-4F38-BC7A-1D622DC69B41` | Mouth pressed or tight |
| `A1D4672B-2E01-435A-BD0D-ABAEB1F4CB6E` | Nose wrinkle |

The possible values for a whole facial expression are:

| Identifier | Whole facial expression |
| --- | --- |
| `E24480FE-8ECF-412C-8A02-3E924971A840` | Brow furrow, eyes widened, and mouth pressed tight |
| `1F26EABE-8350-48C5-97F0-06EFD6FEC6C4` | Baseline |
| `726DA5E5-E63A-43CC-B7F3-FDD42A5583FA` | Nose wrinkle or upper lip raise |
| `6AEC22CC-2311-45F1-AF8E-F372A3C979B2` | Brow raise with furrow, eyes widened, and mouth stretch |
| `FECC0DAC-9B31-4504-896E-6C2898F16B69` | Lip raise and cheek raise |
| `A1E9B99B-C90B-4DB4-8ED3-4E0382ABC8B5` | Inner brow raise and mouth corner depress |
| `C57C8CCA-0194-4327-8CBA-987FAF744096` | Brow raise without furrow, eyes widened, and jaw drop |

## See Also

- [var value: Double](srfacemetricsexpression/value.md)
  The current position of the expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srfacemetricsexpression/identifier)*