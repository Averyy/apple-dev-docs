# nibName

**Framework**: AppKit  
**Kind**: property

The name of the nib file to be loaded to instantiate the receiver’s primary view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var nibName: NSNib.Name? { get }
```

#### Discussion

This property’s value is the name you provide to the `nibNameOrNil` parameter in the [`init(nibName:bundle:)`](nsviewcontroller/init(nibname:bundle:).md) method.

## See Also

- [init(nibName: NSNib.Name?, bundle: Bundle?)](nsviewcontroller/init(nibname:bundle:).md)
  Returns a view controller object initialized to the nib file in the specified bundle.
- [var nibBundle: Bundle?](nsviewcontroller/nibbundle.md)
  The nib bundle to be loaded to instantiate the receiver’s primary view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/nibname)*