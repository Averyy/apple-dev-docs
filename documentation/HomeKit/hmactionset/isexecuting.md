# isExecuting

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

The execution status of the action set.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isExecuting: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isExecuting) BOOL executing;
```

#### Discussion

[`true`](../../Swift/true.md) while executing, otherwise [`false`](../../Swift/false.md).

## See Also

### Keeping track of execution
- [var lastExecutionDate: Date?](./lastexecutiondate.md)
  The last execution date of the action set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmactionset/isexecuting)*