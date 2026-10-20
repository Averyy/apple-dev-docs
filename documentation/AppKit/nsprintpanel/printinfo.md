# printInfo

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The information associated with the running Print panel.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var printInfo: NSPrintInfo { get }
```

```objc
@property (strong, readonly) NSPrintInfo * printInfo;
```

#### Discussion

The value in this property is `nil` if the Print panel is not currently running.

## See Also

### Accessing the Printing Information
- [class NSPrintInfo](../nsprintinfo.md)
  An object that stores information that’s used to generate printed output.
- [NSPrintPanel.Result](./result.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintpanel/printinfo)*