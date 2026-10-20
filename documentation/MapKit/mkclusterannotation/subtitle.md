# subtitle

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The subtitle string to display for the group of annotations.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var subtitle: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * subtitle;
```

#### Discussion

The cluster annotation object sets this property to a string that conveys how many additional annotations the group includes, except for the annotation with the title that the [`title`](./title.md) property displays.

## See Also

### Getting the cluster attributes
- [var title: String?](./title.md)
  The title string to display for the group of annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkclusterannotation/subtitle)*