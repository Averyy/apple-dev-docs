# CPAlertActionHandler

**Framework**: CarPlay  
**Kind**: typealias  
**Role**: Type Alias

The declaration for an alert action handler.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+

## Declaration

```swift
typealias CPAlertActionHandler = (CPAlertAction) -> Void
```

```c
typedef void (^)(CPAlertAction *) CPAlertActionHandler;
```

## Parameters

- `action`: The alert action that invoked the block.

## See Also

### Getting the Action Handler
- [var handler: CPAlertActionHandler](./cpalertaction/handler.md)
  The closure that CarPlay invokes after the user taps the action button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpalertactionhandler)*