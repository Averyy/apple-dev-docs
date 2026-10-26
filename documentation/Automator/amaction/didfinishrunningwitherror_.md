# didFinishRunningWithError:

**Framework**: Automator  
**Kind**: method  
**Role**: Instance Method

Sent by the action to itself when it has finished running asynchronously.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.5+ - Deprecated in 10.5

> **Deprecated**: Use [`finishRunningWithError(_:)`](./finishrunningwitherror%28_%29.md) instead.

## Declaration

```objc
- (void) didFinishRunningWithError:(NSDictionary<NSString *,id> *) errorInfo;
```

#### Discussion

An action that overrides [`runAsynchronously(withInput:)`](./runasynchronously%28withinput%29.md) should invoke `didFinishRunningWithError:` on completion, so that Automator can resume running the workflow that the action is part of.

## Parameters

- `errorInfo`: If an error occurred during asynchronous running of the action, upon return contains an instance of `NSError` that describes the problem.

## See Also

### Deprecated
- [- runWithInput:fromAction:error:](./runwithinput_fromaction_error_.md)
  Requests the action to perform its task using the specified input from the specified action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amaction/didfinishrunningwitherror:)*