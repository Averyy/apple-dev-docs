# NSViewController.ViewLoading

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

A property wrapper that loads the view controller’s view before accessing the property.

**Availability**:
- macOS 13.3+
- Swift 5.1+

## Declaration

```swift
@propertyWrapper
struct ViewLoading<Value>
```

#### Overview

Use this property wrapper on view controller properties that can be `nil` before the view controller’s view loads. Wrapping view controller properties this way eliminates crashes that can occur from implicitly defining properties as [`Optional`](../../Swift/optional.md), and then referencing them before the view controller finishes loading.

The following example uses the `NSViewController.ViewLoading` wrapper to ensure that `dateLabel` [`NSTextField`](../nstextfield.md) loads before referencing it in the `didSet` of the `date` property observer:

```swift
class DateViewController: NSViewController {
    @ViewLoading private var dateLabel: NSTextField
    
    var date: Date? {
        didSet {
            let dateFormatter = DateFormatter()
            dateFormatter.dateStyle = .full
            let dateString = dateFormatter.string(from: self.date ?? Date())
            self.dateLabel.stringValue = dateString
        }
    }
}
```

After loading [`NSTextField`](../nstextfield.md), the system can safely access and set the `date` property.

```swift
let dateViewController = DateViewController()
dateViewController.date = Date()
```

Use this property wrapper over implicitly unwrapped optionals for `IBOutlets` as well.

```swift
@IBOutlet @ViewLoading private var dateLabel: NSTextField
```

## Topics

### Creating a ViewLoading Property Wrapper
- [init()](./viewloading/init%28%29.md)
  Creates an empty property wrapper that loads the view controller’s view before accessing the property.
- [init(wrappedValue: Value)](./viewloading/init%28wrappedvalue%29.md)
  Creates a property wrapper that loads the view controller’s view before accessing the property.

## See Also

### Related Documentation
- [NSWindowController.WindowLoading](../nswindowcontroller/windowloading.md)
  A property wrapper that loads the receiver’s window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/viewloading)*