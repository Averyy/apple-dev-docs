# ODQueryDelegate

**Framework**: Open Directory  
**Kind**: protocol  
**Role**: Protocol

The `ODQueryDelegate` protocol defines methods for receiving results returned from an Open Directory query.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
protocol ODQueryDelegate : NSObjectProtocol
```

```objc
@protocol ODQueryDelegate <NSObject>
```

## Topics

### Receiving results from a scheduled query
- [func query(ODQuery!, foundResults: [Any]!, error: (any Error)!)](./odquerydelegate/query%28_,foundresults,error%29.md)
  The delegate method called as results are returned from a query scheduled in a run loop.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odquerydelegate)*