# view(withFrame:filter:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Type Method

Creates a view that contains controls for the input parameters of a filter.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class func view(withFrame frameRect: NSRect, filter inFilter: CIFilter!) -> Any!
```

```objc
+ (id) viewWithFrame:(NSRect) frameRect filter:(CIFilter *) inFilter;
```

## Return Value

An `IKFilterUIView` object that contains controls for the input parameters of the provided filter.

## Parameters

- `frameRect`: The rectangle that defines the area of the view.
- `inFilter`: A Core Image filter. The view retains the filter.

## See Also

### Creating and Initializing a Filter UI View
- [init!(frame: NSRect, filter: CIFilter!)](./init%28frame,filter%29.md)
  Initializes a view that contains controls for the input parameters of a filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikfilteruiview/view(withframe:filter:))*