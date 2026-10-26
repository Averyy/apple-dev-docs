# initWithInkType:color:width:identifier:

**Framework**: PencilKit  
**Kind**: method  
**Role**: Instance Method

Creates a new inking item with the specified ink type, color, width, and identifier.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 26.0+
- visionOS 2.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```objc
- (instancetype) initWithInkType:(PKInkType) inkType color:(UIColor *) color width:(CGFloat) width identifier:(NSString *) identifier;
```

*macOS*

```objc
- (instancetype) initWithInkType:(PKInkType) inkType color:(NSColor *) color width:(CGFloat) width identifier:(NSString *) identifier;
```

## See Also

### Creating an inking item
- [- initWithInkType:color:width:](./initwithinktype_color_width_.md)
  Creates a new inking item with the specified ink type, color, and width.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktoolpickerinkingitem/initwithinktype:color:width:identifier:)*