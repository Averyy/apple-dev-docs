# init(frame:filter:)

**Framework**: Quartz  
**Kind**: init

Initializes a view that contains controls for the input parameters of a filter.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
init!(frame frameRect: NSRect, filter inFilter: CIFilter!)
```

#### Return Value

The  `IKFilterUIView` object initialized with controls for the input parameters of the provided filter.

## Parameters

- `frameRect`: The rectangle that defines the area of the view.
- `inFilter`: A Core Image filter. The view retains the filter.

## See Also

- [class func view(withFrame: NSRect, filter: CIFilter!) -> Any!](ikfilteruiview/view(withframe:filter:).md)
  Creates a view that contains controls for the input parameters of a filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikfilteruiview/init(frame:filter:))*