# notifyRulesChanged()

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Notify the Filter Data Provider that the filtering rules have changed on disk.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func notifyRulesChanged()
```

```objc
- (void) notifyRulesChanged;
```

#### Discussion

The Filter Control Provider can call this method to notify the Filter Data Provider that the rules changed. It is only necessary to call this method when the update to the rules was not a direct result of a call to [`handleNewFlow(_:completionHandler:)`](./handlenewflow%28_,completionhandler%29.md).

## See Also

### Handling requests for new rules
- [func handleNewFlow(NEFilterFlow, completionHandler: (NEFilterControlVerdict) -> Void)](./handlenewflow%28_,completionhandler%29.md)
  Handle a request for new filtering rules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltercontrolprovider/notifyruleschanged())*