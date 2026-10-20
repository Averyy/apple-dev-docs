# setImage(_:at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

*Mac Catalyst*

```swift
func setImage(_ image: UIImage?, at index: Int)
```

*macOS*

```swift
func setImage(_ image: NSImage?, at index: Int)
```

*Mac Catalyst*

```objc
- (void) setImage:(UIImage *) image atIndex:(NSInteger) index;
```

*macOS*

```objc
- (void) setImage:(NSImage *) image atIndex:(NSInteger) index;
```

## See Also

### Configuring picker appearance
- [var numberOfOptions: Int](./numberofoptions.md)
- [func setLabel(String, at: Int)](./setlabel%28_,at%29.md)
- [func label(at: Int) -> String?](./label%28at%29.md)
- [func image(at: Int) -> UIImage?](./image%28at%29.md)
- [var collapsedRepresentationImage: UIImage?](./collapsedrepresentationimage.md)
- [var collapsedRepresentationLabel: String](./collapsedrepresentationlabel.md)
- [var controlRepresentation: NSPickerTouchBarItem.ControlRepresentation](./controlrepresentation-swift.property.md)
- [NSPickerTouchBarItem.ControlRepresentation](./controlrepresentation-swift.enum.md)
  Constants that specify display styles for picker bar items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspickertouchbaritem/setimage(_:at:))*