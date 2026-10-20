# makeUserDataOrSource(queue:)

**Framework**: Dispatch  
**Kind**: method  
**Role**: Type Method

Creates a new dispatch source object that you use to coalesce custom app data using an OR operator.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
class func makeUserDataOrSource(queue: DispatchQueue? = nil) -> any DispatchSourceUserDataOr
```

#### Return Value

A dispatch source object that conforms to the [`DispatchSourceUserDataOr`](../dispatchsourceuserdataor.md) protocol.

#### Discussion

After creating the dispatch source, use the methods of the [`DispatchSourceProtocol`](../dispatchsourceprotocol.md) protocol to install the event handlers you need. The returned dispatch source is in the inactive state initially. When you are ready to begin processing events, call its [`activate()`](../dispatchobject/activate%28%29.md) method.

## Parameters

- `queue`: The dispatch queue to use when executing the installed handlers.

## See Also

### Creating a Custom Source
- [class func makeUserDataAddSource(queue: DispatchQueue?) -> any DispatchSourceUserDataAdd](./makeuserdataaddsource%28queue%29.md)
  Creates a new dispatch source object that you use to coalesce custom app data using an AND operator.
- [class func makeUserDataReplaceSource(queue: DispatchQueue?) -> any DispatchSourceUserDataReplace](./makeuserdatareplacesource%28queue%29.md)
  Creates a new dispatch source object that you use to track custom app data.
- [protocol DispatchSourceUserDataAdd](../dispatchsourceuserdataadd.md)
  A dispatch source that coalesces data you provide using an AND operation.
- [protocol DispatchSourceUserDataOr](../dispatchsourceuserdataor.md)
  A dispatch source that coalesces data you provide using an OR operation.
- [protocol DispatchSourceUserDataReplace](../dispatchsourceuserdatareplace.md)
  A dispatch source that replaces any pending data with the new value you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsource/makeuserdataorsource(queue:))*