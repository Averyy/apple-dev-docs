# init

**Framework**: DriverKit  
**Kind**: method

Handles the basic initialization of the dispatch source.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
bool init();
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if initialization was successful, or [`false`](https://developer.apple.com/documentation/Swift/false) if an error occurred.

#### Discussion

Don’t call this method directly. Call [`Create`](iotimerdispatchsource/create.md) when you want to create a new timer dispatch queue.

## See Also

- [Create](iotimerdispatchsource/create.md)
  Creates and configures a timer dispatch object.
- [free](iotimerdispatchsource/free.md)
  Performs any final cleanup for the timer dispatch source.
- [SetHandler](iotimerdispatchsource/sethandler.md)
  Sets the handler block to run when the timer fires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iotimerdispatchsource/init)*