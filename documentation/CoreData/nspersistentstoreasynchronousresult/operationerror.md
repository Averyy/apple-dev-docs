# operationError

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

An error that contains details if the asynchronous fetch request fails.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var operationError: (any Error)? { get }
```

```objc
@property (strong, readonly, nullable) NSError * operationError;
```

## See Also

### Inspecting the Result
- [var managedObjectContext: NSManagedObjectContext](./managedobjectcontext.md)
  The managed object context for the result.
- [var progress: Progress?](./progress.md)
  An object that reports progress for the asynchronous fetch request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstoreasynchronousresult/operationerror)*