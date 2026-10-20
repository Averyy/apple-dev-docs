# init(defaults:initialValues:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Returns an initialized NSUserDefaultsController object using the NSUserDefaults instance specified in `defaults` and the initial default values contained in the `initialValues` dictionary.

**Availability**:
- macOS

## Declaration

```swift
init(defaults: UserDefaults?, initialValues: [String : Any]?)
```

```objc
- (instancetype) initWithDefaults:(NSUserDefaults *) defaults initialValues:(NSDictionary<NSString *,id> *) initialValues;
```

#### Discussion

If `defaults` is `nil`, the receiver uses `[NSUserDefaults standardUserDefaults]`.

This method is the designated initializer.

## See Also

### Initializing a user defaults controller
- [init?(coder: NSCoder)](./init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserdefaultscontroller/init(defaults:initialvalues:))*