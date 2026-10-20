# nameVariants

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

nameVariants is an array of @c NSString representing variants of the waypoint’s display name, arranged from most to least preferred. The variant strings should be provided as localized, displayable content.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
var nameVariants: [String] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSString *> * nameVariants;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationwaypoint/namevariants)*