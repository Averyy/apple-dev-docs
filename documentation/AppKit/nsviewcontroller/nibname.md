# nibName

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The name of the nib file to be loaded to instantiate the receiver’s primary view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var nibName: NSNib.Name? { get }
```

```objc
@property (copy, readonly, nullable) NSNibName nibName;
```

#### Discussion

This property’s value is the name you provide to the `nibNameOrNil` parameter in the [`init(nibName:bundle:)`](./init%28nibname,bundle%29.md) method.

## See Also

### Related Documentation
- [init(nibName: NSNib.Name?, bundle: Bundle?)](./init%28nibname,bundle%29.md)
  Returns a view controller object initialized to the nib file in the specified bundle.
### Nib Properties
- [var nibBundle: Bundle?](./nibbundle.md)
  The nib bundle to be loaded to instantiate the receiver’s primary view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/nibname)*