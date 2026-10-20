# delegate

**Framework**: Core WLAN  
**Kind**: property  
**Role**: Instance Property

An object that provides Wi-Fi event handling.

**Availability**:
- macOS 10.10+

## Declaration

```swift
weak var delegate: AnyObject? { get set }
```

```objc
@property (nonatomic, weak) id delegate;
```

#### Discussion

When a client registers for Wi-Fi events with the [`startMonitoringEvent(with:)`](./startmonitoringevent%28with%29.md) method, the client’s delegate receives messages in response to Wi-Fi events. The delegate should adopt the [`CWEventDelegate`](../cweventdelegate.md) protocol to receive these messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwwificlient/delegate)*