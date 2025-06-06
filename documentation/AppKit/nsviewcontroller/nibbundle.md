# nibBundle

**Framework**: AppKit  
**Kind**: property

The nib bundle to be loaded to instantiate the receiver’s primary view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var nibBundle: Bundle? { get }
```

#### Discussion

This property’s value is the bundle you provide to the `nibBundleOrNil` parameter in the [`init(nibName:bundle:)`](nsviewcontroller/init(nibname:bundle:).md) method.

## See Also

- [var nibName: NSNib.Name?](nsviewcontroller/nibname.md)
  The name of the nib file to be loaded to instantiate the receiver’s primary view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/nibbundle)*