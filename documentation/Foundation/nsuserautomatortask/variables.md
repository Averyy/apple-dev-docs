# variables

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The variables required by the Automator workflow.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var variables: [String : Any]? { get set }
```

```objc
@property (copy, nullable) NSDictionary<NSString *,id> * variables;
```

## See Also

### Executing Automator Tasks
- [func execute(withInput: (any NSSecureCoding)?, completionHandler: NSUserAutomatorTask.CompletionHandler?)](./execute%28withinput,completionhandler%29.md)
  Execute the Automator workflow by providing it as securely coded input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuserautomatortask/variables)*