# listAvailableTestingOperations()

**Framework**: File Provider  
**Kind**: method  
**Role**: Instance Method

Lists all the operations that are ready for scheduling.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
func listAvailableTestingOperations() throws -> [any NSFileProviderTestingOperation]
```

```objc
- (NSArray<id<NSFileProviderTestingOperation>> *) listAvailableTestingOperationsWithError:(NSError **) error;
```

## Discussion

> ❗ **Important**:  Before calling this method, you must set the domain’s [`testingModes`](../nsfileproviderdomain/testingmodes-swift.property.md) property to include the [`interactive`](../nsfileproviderdomain/testingmodes-swift.struct/interactive.md) value.

The system waits for all the pending disk and working set updates before returning the list of available operations. The operations that it returns may become invalid if the system receives new events, or when you schedule and execute operations using the [`run(_:)`](./run%28_%29.md) method.

## See Also

### Testing
- [func run([any NSFileProviderTestingOperation]) throws -> [AnyHashable : any Error]](./run%28_%29.md)
  Asks the system to schedule and execute the specified operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/listavailabletestingoperations())*