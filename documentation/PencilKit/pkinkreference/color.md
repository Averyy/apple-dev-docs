# color

**Framework**: PencilKit  
**Kind**: property  
**Role**: Instance Property

The base color for this ink.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
var color: UIColor { get }
```

*macOS*

```swift
var color: NSColor { get }
```

*iOS, iPadOS, Mac Catalyst, visionOS*

```objc
@property (nonatomic, readonly) UIColor * color;
```

*macOS*

```objc
@property (nonatomic, readonly) NSColor * color;
```

## See Also

### Getting the ink attributes
- [var inkType: __PKInkType](./inktype.md)
  The type of ink, such as pen or pencil, as defined in the [`PKInkType`](../pkinktype.md) enumeration.
- [PKInkType](../pkinktype.md)
  The type that defines the shape of stroked lines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkinkreference/color)*