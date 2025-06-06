# NSWindowController.WindowLoading

**Framework**: AppKit  
**Kind**: struct

A property wrapper that loads the receiver’s window.

**Availability**:
- macOS 13.3+
- Swift 5.1+

## Declaration

```swift
@propertyWrapper
struct WindowLoading<Value>
```

#### Overview

Use this property wrapper on window controller properties that can be `nil` before the window controller’s window loads. Wrapping window controller properties this way eliminates crashes that can occur from implicitly defining properties as [`Optional`](https://developer.apple.com/documentation/Swift/Optional), and then referencing them before the window controller finishes loading.

The following example uses the `NSWindowController.WindowLoading` property wrapper to ensure that `dateLabel` [`NSTextField`](nstextfield.md) loads before referencing it in the `didSet` of the `date` property observer:

```swift
class DateWindowController: NSWindowController {
    @WindowLoading private var dateLabel: NSTextField
    
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

After loading [`NSTextField`](nstextfield.md), the system can safely access and set the `date` property.

```swift
let dateWindowController = DateWindowController()
dateWindowController.date = Date()
```

Use this property wrapper over implicitly unwrapped optionals for `IBOutlets` as well.

```swift
@IBOutlet @WindowLoading private var dateLabel: NSTextField
```

## Topics

### Creating a WindowLoading Property Wrapper
- [init()](nswindowcontroller/windowloading/init.md)
  Creates an empty property wrapper that loads the window controller’s window before accessing the property.
- [init(wrappedValue: Value)](nswindowcontroller/windowloading/init(wrappedvalue:).md)
  Creates a property wrapper that loads the window controller’s window before accessing the property.

## See Also

- [NSViewController.ViewLoading](nsviewcontroller/viewloading.md)
  A property wrapper that loads the view controller’s view before accessing the property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/windowloading)*