# MKAddressRepresentations.ContextStyle

**Framework**: MapKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum MKAddressRepresentationsContextStyle : NSInteger;
```

## Discussion

Use the [`MKAddressRepresentations.ContextStyle`](./contextstyle.md) to configure the degree of disambiguation context to include in an address representation from [`MKAddressRepresentations`](../mkaddressrepresentations.md), such as including the region name with the city.

## Topics

### Creating a context style
- [init?(rawValue: Int)](./contextstyle/init%28rawvalue%29.md)
  Initializes a context style with the raw value you provide.
### Available context styles
- [MKAddressRepresentations.ContextStyle.automatic](./contextstyle/automatic.md)
  The value that represents the automatic context style.
- [MKAddressRepresentations.ContextStyle.short](./contextstyle/short.md)
  The value that represents the short context style.
- [MKAddressRepresentations.ContextStyle.full](./contextstyle/full.md)
  The value that represents the full context style.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkaddressrepresentations/contextstyle)*