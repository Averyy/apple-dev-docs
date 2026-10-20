# variationAxisDefaultValue

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Type Property

The key used to obtain the default variation axis value from a variation axis dictionary.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class let variationAxisDefaultValue: CFString
```

```c
extern CFStringRef const kCGFontVariationAxisDefaultValue;
```

#### Discussion

The value obtained with this key is a [`CFNumber`](../../CoreFoundation/cfnumber.md) that specifies the default value of the variation axis.

## See Also

### Constants
- [class let variationAxisName: CFString](./variationaxisname.md)
  The key used to obtain the variation axis name from a variation axis dictionary.
- [class let variationAxisMinValue: CFString](./variationaxisminvalue.md)
  The key used to obtain the minimum variation axis value from a variation axis dictionary.
- [class let variationAxisMaxValue: CFString](./variationaxismaxvalue.md)
  The key used to obtain the maximum variation axis value from a variation axis dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgfont/variationaxisdefaultvalue)*