# CPAlertActionHandler

**Framework**: CarPlay  
**Kind**: typealias

The declaration for an alert action handler.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+

## Declaration

```swift
typealias CPAlertActionHandler = (CPAlertAction) -> Void
```

## Parameters

- `action`: The alert action that invoked the block.

## See Also

- [var handler: CPAlertActionHandler](cpalertaction/handler.md)
  The closure that CarPlay invokes after the user taps the action button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpalertactionhandler)*