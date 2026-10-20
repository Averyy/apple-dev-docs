# title

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The title string to display for the group of annotations.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var title: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * title;
```

#### Discussion

The cluster annotation object automatically sets this string to the title of one of the annotations in its group.

## See Also

### Getting the cluster attributes
- [var subtitle: String?](./subtitle.md)
  The subtitle string to display for the group of annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkclusterannotation/title)*