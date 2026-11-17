# addressVariants

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

addressVariants is an array of @c NSString representing variants of the waypoint’s address, arranged from most to least preferred. The variant strings should be provided as localized, displayable content.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
var addressVariants: [String] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSString *> * addressVariants;
```

## See Also

### Getting the route information
- [var nameVariants: [String]](./namevariants.md)
  nameVariants is an array of @c NSString representing variants of the waypoint’s display name, arranged from most to least preferred. The variant strings should be provided as localized, displayable content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationwaypoint/addressvariants)*