# name

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The name of the operation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var name: String? { get set }
```

```objc
@property (copy, nullable) NSString * name;
```

#### Discussion

Assign a name to the operation object to help identify it during debugging.

## See Also

### Getting the Operation Status
- [var isCancelled: Bool](./iscancelled.md)
  A Boolean value indicating whether the operation has been cancelled
- [var isExecuting: Bool](./isexecuting.md)
  A Boolean value indicating whether the operation is currently executing.
- [var isFinished: Bool](./isfinished.md)
  A Boolean value indicating whether the operation has finished executing its task.
- [var isConcurrent: Bool](./isconcurrent.md)
  A Boolean value indicating whether the operation executes its task asynchronously.
- [var isAsynchronous: Bool](./isasynchronous.md)
  A Boolean value indicating whether the operation executes its task asynchronously.
- [var isReady: Bool](./isready.md)
  A Boolean value indicating whether the operation can be performed now.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operation/name)*