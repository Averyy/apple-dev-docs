# MKAddressRepresentations.ContextStyle

**Framework**: MapKit  
**Kind**: enum

Values that describe the degree of disambiguation context to include in an address representation.

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
enum ContextStyle
```

#### Discussion

Use the [`MKAddressRepresentations.ContextStyle`](mkaddressrepresentations/contextstyle.md) to configure the degree of disambiguation context to include in an address representation from [`MKAddressRepresentations`](mkaddressrepresentations.md), such as including the region name with the city.

## Topics

### Creating a context style
- [init?(rawValue: Int)](mkaddressrepresentations/contextstyle/init(rawvalue:).md)
  Initializes a context style with the raw value you provide.
### Available context styles
- [MKAddressRepresentations.ContextStyle.automatic](mkaddressrepresentations/contextstyle/automatic.md)
  The value that represents the automatic context style.
- [MKAddressRepresentations.ContextStyle.short](mkaddressrepresentations/contextstyle/short.md)
  The value that represents the short context style.
- [MKAddressRepresentations.ContextStyle.full](mkaddressrepresentations/contextstyle/full.md)
  The value that represents the full context style.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkaddressrepresentations/contextstyle)*