# delegate

**Framework**: Core WLAN  
**Kind**: property

An object that provides Wi-Fi event handling.

**Availability**:
- macOS 10.10+

## Declaration

```swift
weak var delegate: AnyObject? { get set }
```

#### Discussion

When a client registers for Wi-Fi events with the [`startMonitoringEvent(with:)`](cwwificlient/startmonitoringevent(with:).md) method, the client’s delegate receives messages in response to Wi-Fi events. The delegate should adopt the [`CWEventDelegate`](cweventdelegate.md) protocol to receive these messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwwificlient/delegate)*