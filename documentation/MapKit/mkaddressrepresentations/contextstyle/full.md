# MKAddressRepresentations.ContextStyle.full

**Framework**: MapKit  
**Kind**: case  
**Role**: Case

The value that represents the full context style.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
case full
```

```c
MKAddressRepresentationsContextStyleFull
```

#### Discussion

The value that tells the framework to include all relevant context. For example, when used with [`cityWithContext(_:)`](../citywithcontext%28_%29.md) MapKit always includes the region name if the device is in that region.

## See Also

### Available context styles
- [MKAddressRepresentations.ContextStyle.automatic](./automatic.md)
  The value that represents the automatic context style.
- [MKAddressRepresentations.ContextStyle.short](./short.md)
  The value that represents the short context style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkaddressrepresentations/contextstyle/full)*