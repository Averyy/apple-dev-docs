# init(defaults:initialValues:)

**Framework**: AppKit  
**Kind**: init

Returns an initialized NSUserDefaultsController object using the NSUserDefaults instance specified in `defaults` and the initial default values contained in the `initialValues` dictionary.

**Availability**:
- macOS ?+

## Declaration

```swift
init(defaults: UserDefaults?, initialValues: [String : Any]?)
```

#### Discussion

If `defaults` is `nil`, the receiver uses `[NSUserDefaults standardUserDefaults]`.

This method is the designated initializer.

## See Also

- [init?(coder: NSCoder)](nsuserdefaultscontroller/init(coder:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserdefaultscontroller/init(defaults:initialvalues:))*