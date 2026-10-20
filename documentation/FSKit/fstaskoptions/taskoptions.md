# taskOptions

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

An array of strings that represent command-line options for the task.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var taskOptions: [String] { get }
```

```objc
@property (copy, readonly) NSArray<NSString *> * taskOptions;
```

#### Discussion

This property is equivalent to the `argv` array of C strings passed to a command-line tool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fstaskoptions/taskoptions)*