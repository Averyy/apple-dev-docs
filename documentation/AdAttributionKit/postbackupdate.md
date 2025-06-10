# PostbackUpdate

**Framework**: AdAttributionKit  
**Kind**: struct

Values you use to update properties in a postback, such as the conversion value.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+

## Declaration

```swift
struct PostbackUpdate
```

## Mentions

- [Identifying conversion values with conversion tags](conversion-tags.md)

## Topics

### Initializers
- [init(fineConversionValue: Int, lockPostback: Bool, coarseConversionValue: CoarseConversionValue?, conversionTypes: [PostbackUpdate.ConversionType]?)](postbackupdate/init(fineconversionvalue:lockpostback:coarseconversionvalue:conversiontypes:).md)
  Creates a new postback update with the conversions values, conversion types, and lock indication you provide.
- [init(fineConversionValue: Int, lockPostback: Bool, conversionTag: String, coarseConversionValue: CoarseConversionValue?, conversionTypes: [PostbackUpdate.ConversionType]?)](postbackupdate/init(fineconversionvalue:lockpostback:conversiontag:coarseconversionvalue:conversiontypes:).md)
### Instance Properties
- [let coarseConversionValue: CoarseConversionValue?](postbackupdate/coarseconversionvalue.md)
  An enumeration that represents the coarse conversion value.
- [let conversionTag: String?](postbackupdate/conversiontag.md)
- [let conversionTypes: [PostbackUpdate.ConversionType]?](postbackupdate/conversiontypes.md)
  An array conversion type the system uses to determine which postbacks to update with this postback update.
- [let fineConversionValue: Int](postbackupdate/fineconversionvalue.md)
  An integer that represents the fine conversion value.
- [let lockPostback: Bool](postbackupdate/lockpostback.md)
  A Boolean value that indicates whether the system should lock the postback, reducing system time deliver a signal
### Enumerations
- [PostbackUpdate.ConversionType](postbackupdate/conversiontype.md)
  Values that describe the types of conversions.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct Postback](postback.md)
  A structure that provides methods you use to update conversion values for ad attributions.
- [enum CoarseConversionValue](coarseconversionvalue.md)
  Values that describe developer-defined, relative-attribution conversion values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/adattributionkit/postbackupdate)*