# weight

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Instance Property

A value between 0 and 1 representing relative significance of the element in its section.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var weight: Double { get }
```

```objc
@property (nonatomic, readonly) double weight;
```

## Discussion

Values range from `0.0` to `1.0` where a higher number represents higher overall significance within the project section. The default value is `0.5`.

Projects that allow a user to reduce the number of elements in a section can use this hint to determine which elements are most important to preserving context.

## See Also

### Describing Project Elements
- [var placement: CGRect](./placement.md)
  A rectangle defining where an element is placed in grid space coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojectelement/weight)*