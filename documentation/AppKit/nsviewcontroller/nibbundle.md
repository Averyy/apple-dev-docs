# nibBundle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The nib bundle to be loaded to instantiate the receiver’s primary view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var nibBundle: Bundle? { get }
```

```objc
@property (strong, readonly, nullable) NSBundle * nibBundle;
```

#### Discussion

This property’s value is the bundle you provide to the `nibBundleOrNil` parameter in the [`init(nibName:bundle:)`](./init%28nibname,bundle%29.md) method.

## See Also

### Nib Properties
- [var nibName: NSNib.Name?](./nibname.md)
  The name of the nib file to be loaded to instantiate the receiver’s primary view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/nibbundle)*