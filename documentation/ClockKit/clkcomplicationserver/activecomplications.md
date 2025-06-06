# activeComplications

**Framework**: ClockKit  
**Kind**: property

The active complications for the current app.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var activeComplications: [CLKComplication]? { get }
```

## Mentions

- [Keeping your complications up to date](keeping-your-complications-up-to-date.md)

#### Discussion

This property contains an array of [`CLKComplication`](clkcomplication.md) objects; each represents a version of your complication currently displayed on the clock face. If the property contains an empty array, it means your app has no complications on the active watch face. If it’s `nil`, it means the server is still connecting to the active complications.

There are no guarantees on when the server will connect with the complications. ClockKit sends a [`CLKComplicationServerActiveComplicationsDidChangeNotification`](clkcomplicationserveractivecomplicationsdidchangenotification.md) notification when the server connects, and the system guarantees that the [`activeComplications`](clkcomplicationserver/activecomplications.md) property has a non-`nil` value after it sends the notification.

To avoid any race conditions, always perform the following steps in order:

1. Set up an observer for the [`CLKComplicationServerActiveComplicationsDidChangeNotification`](clkcomplicationserveractivecomplicationsdidchangenotification.md) notification.
2. Check and see if [`activeComplications`](clkcomplicationserver/activecomplications.md) contains a `nil` value.

If [`activeComplications`](clkcomplicationserver/activecomplications.md) has a non-`nil` value, you can use it immediately. Otherwise, wait for the notification to fire, and then check the [`activeComplications`](clkcomplicationserver/activecomplications.md) property again.

The following code listing shows a safe implementation using Swift’s asynchronous APIs.

```swift
extension CLKComplicationServer {
    
    // Safely access the server's active complications.
    @MainActor
    func getActiveComplications() async -> [CLKComplication] {
        return await withCheckedContinuation { continuation in
            
            // First, set up the notification.
            let center = NotificationCenter.default
            let mainQueue = OperationQueue.main
            var token: NSObjectProtocol?
            token = center.addObserver(forName: .CLKComplicationServerActiveComplicationsDidChange, object: nil, queue: mainQueue) { _ in
                center.removeObserver(token!)
                continuation.resume(returning: self.activeComplications!)
            }
            
            // Then check to see if we have a valid active complications array.
            if activeComplications != nil {
                center.removeObserver(token!)
                continuation.resume(returning: self.activeComplications!)
            }
        }
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationserver/activecomplications)*