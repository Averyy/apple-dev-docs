# init(frame:filter:)

**Framework**: Quartz  
**Kind**: init  
**Role**: Initializer

Initializes a view that contains controls for the input parameters of a filter.

**Availability**:
- macOS 10.4+

## Declaration

```swift
init!(frame frameRect: NSRect, filter inFilter: CIFilter!)
```

```objc
- (id) initWithFrame:(NSRect) frameRect filter:(CIFilter *) inFilter;
```

## Return Value

The  `IKFilterUIView` object initialized with controls for the input parameters of the provided filter.

## Parameters

- `frameRect`: The rectangle that defines the area of the view.
- `inFilter`: A Core Image filter. The view retains the filter.

## See Also

### Creating and Initializing a Filter UI View
- [class func view(withFrame: NSRect, filter: CIFilter!) -> Any!](./view%28withframe,filter%29.md)
  Creates a view that contains controls for the input parameters of a filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikfilteruiview/init(frame:filter:))*