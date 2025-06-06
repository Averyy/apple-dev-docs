# view(withFrame:filter:)

**Framework**: Quartz  
**Kind**: method

Creates a view that contains controls for the input parameters of a filter.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
class func view(withFrame frameRect: NSRect, filter inFilter: CIFilter!) -> Any!
```

#### Return Value

An `IKFilterUIView` object that contains controls for the input parameters of the provided filter.

## Parameters

- `frameRect`: The rectangle that defines the area of the view.
- `inFilter`: A Core Image filter. The view retains the filter.

## See Also

- [init!(frame: NSRect, filter: CIFilter!)](ikfilteruiview/init(frame:filter:).md)
  Initializes a view that contains controls for the input parameters of a filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikfilteruiview/view(withframe:filter:))*