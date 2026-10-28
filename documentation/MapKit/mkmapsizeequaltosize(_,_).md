# MKMapSizeEqualToSize(_:_:)

**Framework**: MapKit  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether two map sizes are equal.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func MKMapSizeEqualToSize(_ size1: MKMapSize, _ size2: MKMapSize) -> Bool
```

```c
static BOOL MKMapSizeEqualToSize(MKMapSize size1, MKMapSize size2);
```

## Return Value

[`true`](../Swift/true.md) if the `width` and `height` values in both sizes are exactly the same, or [`false`](../Swift/false.md) if one or both values are different.

## Parameters

- `size1`: The first map size.
- `size2`: The second map size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapsizeequaltosize(_:_:))*